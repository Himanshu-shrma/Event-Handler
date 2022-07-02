import imp
import re
from urllib import response
from django.shortcuts import redirect, render
import calendar
from calendar import HTMLCalendar
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Event, Venue
from .forms import EventFormAdmin, VenueForm , EventForm,EventFormAdmin
from django.contrib.auth.models import User
from django.contrib import messages
#import for csv download functionality
import csv
from django.http import FileResponse

#import for PDF download functionality
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.contrib.auth.models import User
#import for Pagination
from django.core.paginator import Paginator


# Create your views here.
def home(request,year=datetime.now().year, month=datetime.now().strftime('%B')):
    month=month.capitalize()
    month_number=list(calendar.month_name).index(month)
    cal=HTMLCalendar().formatmonth(year,month_number)
    now=datetime.now()
    time=now.strftime('%I:%M:%S %p')
    if request.user.is_authenticated:
        name=User.objects.get(username=request.user.username).first_name
        event_list=Event.objects.filter(
            event_date__gte =datetime.now(),
            attendees=request.user,
        ).order_by('event_date')
    else:
        return render (request,'events/home.html',
    { 
        'year':year,
        'month':month,
        "cal":cal,
        "time":time,
    })
    
    return render (request,'events/home.html',
    {   'name':name,
        'year':year,
        'month':month,
        "cal":cal,
        "time":time,
        "event_list":event_list,
    })

def all_events(request):
    #event_list=Event.objects.all().order_by('event_date')

    p=Paginator(Event.objects.all().order_by('event_date'),2)
    
    page= request.GET.get('page')
    events=p.get_page(page)
    return render(request,'events/event_list.html',{
        'events':events}
        )

def add_venue(request):
    submitted=False
    if request.method=="POST":
        form=VenueForm(request.POST)
        if form.is_valid():
            venue=form.save(commit=False)
            venue.owner=request.user.id
            venue.save()
            return HttpResponseRedirect("/add_venue?submitted=True")  
    else:
        form=VenueForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'events/add_venue.html',{'form':form,'submitted':submitted})

def list_venues(request):
    venue_list= Venue.objects.all().order_by('name')
    return render(request,'events/venue.html',{
        'venues_list':venue_list
    })

def show_venue(request,venue_id):
    venue=Venue.objects.get(pk=venue_id)
    owner_info= User.objects.get(pk=venue.owner)
    return render(request,'events/show_venue.html',{
        'venue':venue,
        'owner_info':owner_info,
    })

def show_event(request,event_id):
    event=Event.objects.get(pk=event_id)
    return render(request,"events/show_event.html",
    {
        'event':event,
    }
    )

def search_venues(request):
    if request.method == "POST":
        searched_data=request.POST['searched_data']
        venues=Venue.objects.filter(name__contains=searched_data)
        return render(request,'events/search_venues.html',{
            'searched_data':searched_data,
            'venues':venues,
        })
    else:
        return render(request,'events/search_venues.html',{
        })  

def search_events(request):
    if request.method == "POST":
        searched_data=request.POST['searched_data']
        events=Event.objects.filter(name__contains=searched_data)
        return render(request,'events/search_events.html',{
            'searched_data':searched_data,
            'events':events,
        })
    else:
        return render(request,'events/search_events.html',{
        })  

def update_venue(request,venue_id):
    venue=Venue.objects.get(pk=venue_id)
    form=VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('venues-list')
    return render(request,'events/update_venue.html',{
        'venue':venue,
        'form':form,
    })

def add_event(request):
    submitted=False
    if request.method=="POST":
        if request.user.is_superuser:
            form = EventFormAdmin(request.POST)    
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/add_event?submitted=True")  
        else:
            form = EventForm(request.POST)
            if form.is_valid():
                #form.save()   
                event=form.save(commit=False)
                event.manager=request.user
                event.save()
                return HttpResponseRedirect("/add_event?submitted=True")  
    else:
        if request.user.is_superuser:
            form=EventFormAdmin
        else:
            form=EventForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'events/add_event.html',{'form':form,'submitted':submitted})

def update_event(request,event_id):
    event=Event.objects.get(pk=event_id)
    if request.user.is_superuser:
        form=EventFormAdmin(request.POST or None, instance=event)
    else:
        form=EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    return render(request,'events/update_event.html',{
        'event':event, 
        'form':form,
    })

def delete_event(request,event_id):
    event= Event.objects.get(pk=event_id)
    if request.user==event.manager:
        event.delete()
        messages.success(request,("Event Deleted!! "))
        return redirect('list-events')  
    else:
        messages.success(request,("You are not Authorize to do this!! "))
        return redirect('list-events')  
    

def delete_venue(request,venue_id):
    venue=Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('venues-list')

#generating txt file for venues

def venue_txt(request):
    response=HttpResponse(content_type='text/plain')
    response['Content-Disposition']='attachment; filename=venues.txt'
    venues=Venue.objects.all()
    lines=[]
    for venue in venues:
        lines.append(f'Venue name : {venue.name}\nAddress: {venue.address}\nzip_code :  {venue.zip_code}\nphone : {venue.phone}\nweb : {venue.web}\nemail_address : {venue.email_address}\n\n\n')

    response.writelines(lines)        
    return response

def venue_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=venues.csv'
    venues=Venue.objects.all()

    #create a csv Writer(Which will write the content in csv writer)
    writer=csv.writer(response)
    writer.writerow(['Venue Name','Address','Zip_code','Phone','Web Address','Email'])

    for venue in venues:
        writer.writerow([venue.name,venue.address,venue.zip_code,venue.phone,venue.web,venue.email_address])

    return response

#Generate PDF file for venues

def venue_pdf(request):
    #create Bytestream buffer
    buf=io.BytesIO()
    #Create a Canvas
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
    #create a text object
    txtobj=c.beginText()
    txtobj.setTextOrigin(inch,inch)
    txtobj.setFont("Helvetica",14)

    #Add Venues in the pdf
    venues=Venue.objects.all()
    lines=[]
    for venue in venues:
        lines.append('\t')
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zip_code)
        lines.append(venue.phone)
        lines.append(venue.web)
        lines.append(venue.email_address)
        lines.append(" ")
        lines.append("___________________________________________")
        lines.append("___________________________________________")
        lines.append(" ")

    for line in lines:
        txtobj.textLine(line)

    c.drawText(txtobj)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True,filename='Venue.pdf')


#filtering the events and showing the events in which the current logged in user is invited

def my_events(request):
    if request.user.is_authenticated:
        my_event=Event.objects.filter(attendees=request.user.id)
        return render(request,
        'events/my_events.html',
        {
            'my_event':my_event,
        })

    else:
        messages.success(request,("You are not Authorize to View This Page!! "))
        return redirect('home') 

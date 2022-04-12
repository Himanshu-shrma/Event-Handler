import re
from django.shortcuts import redirect, render
import calendar
from calendar import HTMLCalendar
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm



# Create your views here.
def home(request,year=datetime.now().year, month=datetime.now().strftime('%B')):
    month=month.capitalize()
    month_number=list(calendar.month_name).index(month)
    cal=HTMLCalendar().formatmonth(year,month_number)
    now=datetime.now()
    time=now.strftime('%I:%M:%S %p')
    name="Raj"
    return render (request,'events/home.html',
    {   'name':name,
        'year':year,
        'month':month,
        "cal":cal,
        "time":time,
    })

def all_events(request):
    event_list=Event.objects.all()
    return render(request,'events/event_list.html',{
        'event_list':event_list
    })

def add_venue(request):
    submitted=False
    if request.method=="POST":
        form=VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_venue?submitted=True")  
    else:
        form=VenueForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'events/add_venue.html',{'form':form,'submitted':submitted})

def list_venues(request):
    venue_list= Venue.objects.all()
    return render(request,'events/venue.html',{
        'venues_list':venue_list
    })

def show_venue(request,venue_id):
    venue=Venue.objects.get(pk=venue_id)
    return render(request,'events/show_venue.html',{
        'venue':venue,
    })

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
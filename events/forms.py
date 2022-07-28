from django import forms
from django.forms import ModelForm
from .models import Venue , Event

class VenueForm(ModelForm):
    class Meta:
        model=Venue
        fields= ('name', 'address','zip_code','phone','web','email_address','venue_image')
        labels={
            'name':'',
            'address':'',
            'zip_code':'',
            'phone':'',
            'web':'',
            'email_address':'',
            'venue_image':'',
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Name of the venue'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the address'}),
            'zip_code':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the zipcode'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Phone Number'}),
            'web':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the web address'}),
            'email_address':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter the Email Address'}),   
        }

class EventFormAdmin(ModelForm):
    class Meta:
        model=Event
        fields= ('name', 'event_date','venue','manager','attendees','description',)
        labels={
            'name':'',
            'event_date':'YYYY-MM-DD HH:MM:SS',
            'venue':'Venues',
            'attendees':'Attendees',
            'description':'',
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Name of the Event'}),
            'event_date':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Event Date'}),
            'venue':forms.Select(attrs={'class':'form-select','placeholder':'Venue'}),
            'manager':forms.Select(attrs={'class':'form-select','placeholder':'Manager'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Attendees'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
        }

class EventForm(ModelForm):
    class Meta:
        model=Event
        fields= ('name', 'event_date','venue','attendees','description',)
        labels={
            'name':'',
            'event_date':'YYYY-MM-DD HH:MM:SS',
            'venue':'Venues',
            'attendees':'Attendees',
            'description':'',
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Name of the Event'}),
            'event_date':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Event Date'}),
            'venue':forms.Select(attrs={'class':'form-select','placeholder':'Venue'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Attendees'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
        }
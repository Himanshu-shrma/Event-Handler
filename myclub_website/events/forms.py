from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from .models import Venue

class VenueForm(ModelForm):
    class Meta:
        model=Venue
        fields= ('name', 'address','zip_code','phone','web','email_address',)
        labels={
            'name':'',
            'address':'',
            'zip_code':'',
            'phone':'',
            'web':'',
            'email_address':'',
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Name of the venue'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the address'}),
            'zip_code':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the zipcode'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Phone Number'}),
            'web':forms.URLInput(attrs={'class':'form-control','placeholder':'Enter the web address'}),
            'email_address':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter the Email Address'}),
        }
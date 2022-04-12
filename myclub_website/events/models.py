from ctypes import addressof
import email
from multiprocessing import managers
from unicodedata import name
import webbrowser
from django.db import models
from django.contrib.auth.models import User



class Venue(models.Model):
    name=models.CharField('Venue Name ',max_length=120)
    address=models.CharField('Venue Address ',max_length=120)
    zip_code=models.CharField('Venue zipcode ',max_length=15 ,blank=True)
    phone=models.CharField('Venue Number ',max_length=13,blank=True)
    web=models.CharField('Website Address ', max_length=25 ,blank=True)
    email_address=models.EmailField('Venue Email',blank=True)

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email=models.EmailField('User Email')

    def __str__(self):
        return self.FirstName + ' ' + self.LastName


class Event(models.Model):
    name=models.CharField('Event Name',max_length=120)
    event_date=models.DateTimeField('Event Date ')
    venue= models.ForeignKey(Venue,blank=True,null=True,on_delete=models.CASCADE)
    # venue=models.CharField(max_length=120)
    manager= models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    description=models.TextField(blank=True)
    event_hours= models.IntegerField()
    attendees= models.ManyToManyField(MyClubUser)

    def __str__(self):
        return self.name
from dataclasses import fields
from django.contrib import admin
from .models import Venue
from .models import Event
from .models import MyClubUser

#admin.site.register(Venue)
#admin.site.register(Event)
admin.site.register(MyClubUser)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display=('name','address','zip_code','phone','web')
    ordering=('name',)
    search_fields=('name','address',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields=(('name','venue'),('event_date','event_hours'),'manager','description',)
    list_display=('name','event_date',)
    list_filter=('venue', 'event_date',) 
    ordering=('event_date',)
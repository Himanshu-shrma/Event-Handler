from django.urls import path,include
from django.contrib import admin
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('<int:year>/<str:month>/',views.home,name='home'),
    path('events',views.all_events,name='list-events'),
    path('add_venue',views.add_venue,name='add-venue'),
    path('list_venues',views.list_venues,name='venues-list'),
    path('show_venue/<venue_id>',views.show_venue,name='show-venue'),
    path('show_event/<event_id>',views.show_event,name='show_event'),
    path('search_venues',views.search_venues,name='search-venues'),
    path('update_venue/<venue_id>',views.update_venue,name='update-venue'),
    path('add_event',views.add_event,name='add-event'),
    path('update_event/<event_id>',views.update_event,name='update-event'),
    path('delete_event/<event_id>',views.delete_event,name='delete-event'),
    path('delete_venue/<venue_id>',views.delete_venue,name='delete-venue'),
    path('venue_txt',views.venue_txt,name='venue_txt'),
    path('venue_csv',views.venue_csv,name='venue_csv'),
    path('venue_pdf',views.venue_pdf,name='venue_pdf'),
    path('my_events',views.my_events,name='my_events'),
    path('search_events',views.search_events,name='search_events'),
    path('approve_events',views.approve_events,name='approve_events'),
]
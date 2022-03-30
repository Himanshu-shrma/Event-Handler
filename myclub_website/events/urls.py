from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='Home'),
    path('<int:year>/<str:month>/',views.home,name='Home'),
    
]
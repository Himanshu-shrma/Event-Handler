from django.urls import path,include
from . import views

urlpatterns = [
    
    path('login-user',views.login_user,name='login-user'),
    path('logout-user',views.logout_user,name='logout-user'),
    path('register-user',views.register_user,name='register-user'),
]
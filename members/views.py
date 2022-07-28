from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterUserForm
#for regirstration of user
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.cache import cache_control

def register_user(request):
    if request.method=="POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'Signed Up Successfully.')
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request,'authenticate/register_user.html',{
        'form':form,
    })

#@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def logout_user(request):

    if not request.user.is_authenticated:
        return redirect('home')
    messages.success(request,"Log out Successfully")
    logout(request)
    return redirect('home')


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Redirect to a success page.
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,"There was an error loggin in , Check username and password")
            return redirect('login-user')
            # Return an 'invalid login' error messages
    else:
        return render(request,'authenticate/login.html',{})

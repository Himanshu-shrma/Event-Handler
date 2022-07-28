from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterUserForm
#for regirstration of user
from django.contrib.auth.forms import UserCreationForm


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

def logout_user(request):
    request.session.flush()
    messages.success(request,"Log out Successfully")
    logout(request)
    return redirect('home')



def login_user(request):
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

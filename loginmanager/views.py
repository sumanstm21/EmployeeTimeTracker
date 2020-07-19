from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CreateUserForm
# Create your views here.

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Wrong Username or Password')

    context = {}
    return render(request, 'loginmanager/login.html', context)
    # return HttpResponse('Login home page')

def logoutpage(request):
    logout(request)
    return redirect('home')

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was Created for ' + user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'loginmanager/register.html', context)

def forgotpasswordpage(request):
    return render(request, 'loginmanager/password.html')

def error401(request):
    return render(request, 'loginmanager/401.html')

def error404(request):
    return render(request, 'loginmanager/404.html')

def error500(request):
    return render(request, 'loginmanager/500.html')
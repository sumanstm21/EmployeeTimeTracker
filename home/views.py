from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse('This is home page')
    return render(request, 'home/index.html')

def userPage(request):
    # return HttpResponse('This is home page')
    return render(request, 'home/user.html')

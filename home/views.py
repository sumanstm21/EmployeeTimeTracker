from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, admin_only
# Create your views here.

@login_required(login_url='loginmanager-login')
# @allowed_users(allowed_roles=['Admin', 'Subadmin'])
@admin_only
def home(request):
    # return HttpResponse('This is home page')
    return render(request, 'home/index.html')

def userPage(request):
    # return HttpResponse('This is home page')
    return render(request, 'home/user.html')

from gc import get_objects
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from video.models import VideoPlan
import stripe
# from django.http import HttpResponse

stripe.api_key = "sk_test_51KIrEMFYZuypDLyMLWtRBqhgaHAySe1fY6R2evoKBjbe5QqtCqIc3tcRErQLQWjJhRnyuAPvtRZWOBgL0Jzzdo8500QaATotcP"

# Create your views here.
def home(request):
    plans = VideoPlan.objects
    return render(request, 'video/home.html', {'video':plans})

def plan(request, pk):
    plan = get_object_or_404(VideoPlan, pk=pk)
    if plan.premium:
        return redirect('join')
    else:
        return render(request, 'video/plan.html', {'plan':plan})

def join(request):
    return render(request, 'video/join.html')

@login_required(login_url='loginmanager-login')
def checkout(request):
    if request.method == 'POST':
        return redirect('video')
    else:
        coupon = 'none'
        plan = 'monthly'
        price = 1000
        og_dollar = 10
        coupon_dollar = 0
        final_dollar = 10
        if request.method == 'GET' and 'plan' in request.GET:
            if request.GET['plan'] == 'yearly':
                plan = 'yearly'
                price = 10000
                og_dollar = 100
                final_dollar = 100
        return render(request, 'video/checkout.html',
        {'plan':plan,'coupon':coupon,'price':price,'og_dollar':og_dollar,
        'coupon_dollar':coupon_dollar,'final_dollar':final_dollar})

def settings(request):
    return render(request, 'video/settings.html')
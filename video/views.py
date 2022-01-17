from gc import get_objects
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from video.models import VideoPlan, Customer
import stripe
# from django.http import HttpResponse

stripe.api_key = "sk_test_51KIrEMFYZuypDLyMLWtRBqhgaHAySe1fY6R2evoKBjbe5QqtCqIc3tcRErQLQWjJhRnyuAPvtRZWOBgL0Jzzdo8500QaATotcP"

# Create your views here.
def home(request):
    plans = VideoPlan.objects.all()
    return render(request, 'video/home.html', {'plans':plans})

def plan(request, pk):
    plan = get_object_or_404(VideoPlan, pk=pk)
    if plan.premium:
        if request.user.is_authenticated:
            try:
                if request.user.customer.membership:
                    return render(request, 'video/plan.html', {'plan':plan})
            except Customer.DoesNotExist:
                    return redirect('join')        
        return redirect('join')
    else:
        return render(request, 'video/plan.html', {'plan':plan})

def join(request):
    return render(request, 'video/join.html')

@login_required(login_url='loginmanager-login')
def checkout(request):

    try:
        if request.user.customer.membership:
            return redirect('settings')
    except Customer.DoesNotExist:
        pass

    coupons = {'christmas':31, 'newyear':50, 'welcome':10}

    if request.method == 'POST':
        stripe_customer = stripe.Customer.create(email=request.user.email, source=request.POST['stripeToken'])
        plan = 'price_1KIrNZFYZuypDLyMTJBV5Q25'
        if request.POST['plan'] == 'yearly':
            plan = 'price_1KIrNZFYZuypDLyMPEjkOAeC'
        if request.POST['coupon'] in coupons:
            percentage = coupons[request.POST['coupon'].lower()]
            try:
                coupon = stripe.Coupon.create(duration='once', id=request.POST['coupon'].lower(),
                percent_off=percentage)
            except:
                pass
            subscription = stripe.Subscription.create(customer=stripe_customer.id,
            items=[{'plan':plan}], coupon=request.POST['coupon'].lower())
        else:
            subscription = stripe.Subscription.create(customer=stripe_customer.id,
            items=[{'plan':plan}])

        # customer = Customer()
        # customer.user = request.user
        # customer.stripeid = stripe_customer.id
        # customer.membership = True
        # customer.cancel_at_period_end = False
        # customer.stripe_subscription_id = subscription.id
        # customer.save()

        customer = Customer()
        customer.user = request.user
        customer.stripeid = stripe_customer.id
        customer.membership = True
        customer.cancel_at_period_end = False
        customer.stripe_subscription_id = subscription.id
        customer.save()

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
        if request.method == 'GET' and 'coupon' in request.GET:
            print(coupons)
            if request.GET['coupon'].lower() in coupons:
                print('fam')
                coupon = request.GET['coupon'].lower()
                percentage = coupons[request.GET['coupon'].lower()]


                coupon_price = int((percentage / 100) * price)
                price = price - coupon_price
                coupon_dollar = str(coupon_price)[:-2] + '.' + str(coupon_price)[-2:]
                final_dollar = str(price)[:-2] + '.' + str(price)[-2:]
        return render(request, 'video/checkout.html',
        {'plan':plan,'coupon':coupon,'price':price,'og_dollar':og_dollar,
        'coupon_dollar':coupon_dollar,'final_dollar':final_dollar})

def settings(request):
    membership = False
    cancel_at_period_end = False
    if request.method == 'POST':
        subscription = stripe.Subscription.retrieve(request.user.customer.stripe_subscription_id)
        subscription.cancel_at_period_end = True
        request.user.customer.cancel_at_period_end = True
        cancel_at_period_end = True
        subscription.save()
        request.user.customer.save()
    else:
        try:
            if request.user.customer.membership:
                membership = True
            if request.user.customer.cancel_at_period_end:
                cancel_at_period_end = True
        except Customer.DoesNotExist:
            membership = False
    return render(request, 'video/settings.html', {'membership':membership,
    'cancel_at_period_end':cancel_at_period_end})
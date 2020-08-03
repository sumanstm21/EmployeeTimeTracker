from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import datetime
from .forms import DailyLogForm
from .models import DailyLog
# Create your views here.

def timecard(request):
    checkin_check = DailyLog.objects.filter(user_id=request.user.id).last()
    if checkin_check == None:
        checkin_status = 0
        checkin_time = 'You have not checked In'
    else:
        data = DailyLog.objects.filter(user_id=request.user.id).last()
        pk_id = data.id
        checkin_status = data.status
        checkin_time = data.checkin_time
        checkin = DailyLog.objects.get(id=pk_id)

    name = request.user
    context = {'name': name, 'checkin_status': checkin_status, 'checkin_time': checkin_time}
    print(checkin_status)
    if request.method == 'POST':
        if 'checkin' in request.POST:
            form = DailyLogForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('checkin')
                # return render(request, 'timecard/index.html', context)

        elif 'checkout' in request.POST:
            checkin.checkout_message = request.POST['checkout_message']
            checkin.status = 0
            checkin.checkout_time = datetime.now()
            checkin.save()
            # form = DailyLogForm(instance=checkin)
            # form = DailyLogForm(request.POST, instance=checkin)
            # if form.is_valid():
            #     form.save(["checkout_message"])
            return redirect('checkin')

    print(checkin_status)
    return render(request, 'timecard/index.html', context)

    return render(request, 'timecard/index.html')

def record(request):
    pk_id = request.user.id
    records = DailyLog.objects.all().filter(user_id=pk_id)
    context = {'records': records}
    return render(request, 'timecard/record.html', context)
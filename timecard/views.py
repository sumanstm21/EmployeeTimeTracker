from django.shortcuts import render, redirect
import csv
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import DailyLogForm
from .models import DailyLog
from loginmanager.models import *
from .filters import ReportFilter
from django.utils.translation import gettext as _
# Create your views here.
from .serializers import dailylogSerializer


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

def allrecord(request):
    pk_id = request.user.id
    records = DailyLog.objects.all()
    context = {'records': records}
    return render(request, 'timecard/allrecord.html', context)

def report(request):
    records = DailyLog.objects.all()
    myFilter = ReportFilter(request.GET, queryset=records)
    records = myFilter.qs
    context = {'records': records, 'myFilter': myFilter}
    return render(request, 'timecard/report.html', context)

def getreport(request):
    records = DailyLog.objects.all()
    myFilter = ReportFilter(request.GET, queryset=records)
    records = myFilter.qs
    context = {'records': records, 'myFilter': myFilter}
    if request.method == 'GET':
        if 'download' in request.GET:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="file.csv"'
            writer = csv.writer(response)
            writer.writerow([_('Username'), _('CheckIn Time'), _('CheckIN Message'), _('CheckOut Time'), _('CheckOut Message'), _('Duration'), _('Payment')])
            writer.writerow([''])
            total = 0
            rate = 0
            for r in records:
                try:
                    rates = Profile.objects.get(user_id=r.user_id)
                    if rates.rate_per_hour == None:
                        rate = 0
                    else:
                        rate = rates.rate_per_hour
                except:
                    pass

                duration = r.checkout_time - r.checkin_time
                # payment = duration
                days, seconds = duration.days, duration.seconds
                hours = days * 24 + seconds // 3600
                minutes = (seconds % 3600) // 60
                seconds = seconds % 60
                payment = (hours * rate) + (minutes * rate/60) + (seconds * rate/3600)
                total = total + payment
                writer.writerow([r.user.username, r.checkin_time, r.checkin_message, r.checkout_time, r.checkout_message, duration, payment])
                # writer.writerow([days, hours, minutes, seconds])
            writer.writerow([''])
            writer.writerow([_('Total'), '', '', '', '', '', total])
            return response
    return render(request, 'timecard/getreport.html', context)

class DailyLogs(APIView):

    def get(self, request):
        dailylogs = DailyLog.objects.all()
        serializer = dailylogSerializer(dailylogs, many=True)
        return Response(serializer.data)

    def post(self):
        pass
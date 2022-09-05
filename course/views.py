from django.shortcuts import render
from datetime import datetime
# Create your views here.
def learn_django(request):
    cname='DJANGO'
    duration='6 Months'
    seats=10
    django_details={'nm':cname,'du':duration,'st':seats}
    return render(request,'course/courseone.html',django_details)
def learn_python(request):
    cname='PYTHON'
    duration='3 Months'
    seats=60
    django_details={'nm':cname,'du':False,'st':seats}
    return render(request,'course/courseone.html',django_details)
def date_time(request):
    d=datetime.now()
    return render(request,'course/courseone.html',{'dt':d})
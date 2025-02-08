from django.shortcuts import render
from django.http import HttpResponse 
from .models import Departments
from .models import Doctors

def index(request):
    person= {
        'name':'Shanu',
        'age' :23,
        'place':'Valamboor',

    }
    return render(request,'index.html',person)

def About(request):
    return render(request,'about.html')

def Booking(request):
    return render(request,'booking.html')

def Doctors(request):
    dict_doc ={
        'doctors':Doctors.objects.all()

    }
    return render(request,'doctors.html',dict_doc)

def Contact(request):
    return render(request,'contact.html')

def Department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)




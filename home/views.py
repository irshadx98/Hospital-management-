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

from django.shortcuts import render
from .models import Doctors  # Import the Doctors model

def doctors_view(request):
    doctors = Doctors.objects.all()  # Fetch all doctors from the database
    return render(request, 'doctors.html', {'doctors': doctors})

def Contact(request):
    return render(request,'contact.html')

def Department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)




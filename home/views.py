from django.shortcuts import render
from django.http import HttpResponse 
from .models import Departments
from .models import Doctors
from .forms import BookingForm

def index(request):
    person= {
        'name':'Shanu',
        'age' :23,
        'place':'Valamboor',
     
     }
    return render(request,'index.html',person)

def About(request):
    return render(request,'about.html')

from django.shortcuts import render, redirect
from .forms import BookingForm

from django.shortcuts import render, redirect
from .forms import BookingForm

def Booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/confirmation.html')
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request, 'booking.html', dict_form)

from django.shortcuts import render
from .models import Doctors  

def doctors_view(request):
    doctors = Doctors.objects.all()  
    return render(request, 'doctors.html', {'doctors': doctors})

def Contact(request):
    return render(request,'contact.html')

def Department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)




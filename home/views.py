from django.shortcuts import render
from django.http import HttpResponse 
from .models import Departments
from .models import Doctors
from .forms import BookingForm
from .models import Feedback
from django.shortcuts import render, get_object_or_404
from .forms import BookingFormm

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
            # return render(request, 'confirmation.html')
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


def Department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)


def Contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        if name and email and message:
            Feedback.objects.create(name=name, email=email, message=message)
            return redirect("/contact")  

    return render(request, "contact.html")
def analytics_dashboard(request):
    return render(request, 'hospital_analytics/dashboard.html')


def book_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctors, id=doctor_id)
    if request.method == 'POST':
        form = BookingFormm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = BookingForm(initial={'doctor': doctor})
    
    return render(request, 'booking.html', {'form': form, 'doctor': doctor})



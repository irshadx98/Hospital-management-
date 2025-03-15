from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse 
from .models import Departments
from .models import Doctors
from .forms import BookingForm
from .models import Feedback
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
            # Save the feedback to the database
            Feedback.objects.create(name=name, email=email, message=message)
            # Add a success message
            messages.success(request, 'Thank you for your feedback! We will get back to you soon.')
            # Redirect to the same page to avoid form resubmission
            return redirect('contact')  # Replace 'contact' with the name of your URL pattern for this view

    return render(request, "contact.html")
def Booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been successfully submitted!')
            
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request, 'booking.html', dict_form)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  # For success messages
from .models import Doctors, Appointment
from .forms import BookingFormm

def book_doctor(request, doctor_id):
   
    doctor = get_object_or_404(Doctors, id=doctor_id)
    
    if request.method == 'POST':
       
        form = BookingForm(request.POST)
        if form.is_valid():
           
            appointment = form.save(commit=False)
           
            appointment.doc_name = doctor
           
            appointment.save()
            messages.success(request, 'Your appointment has been successfully booked!')
           
            return redirect('doctors')
        else:
            
            print("Form errors:", form.errors)
    else:
        
        
       form = BookingForm(initial={'doc_name': doctor})
    
    
    return render(request, 'Appointment.html', {'form': form, 'doctor': doctor})
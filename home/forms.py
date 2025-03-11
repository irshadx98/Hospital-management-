from django import forms
from .models import Booking
from .models import Appointment

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
        }

        labels = {
            'p_name': "Patient Name:",
            'p_phone': "Patient Phone:",
            'p_email': "Email:",
            'doc_name': "Doctor:",
            'booking_date': "Date"
        }

class BookingFormm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name', 'patient_email', 'patient_phone', 'appointment_date', 'doctor']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
        }

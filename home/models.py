from django.db import models
from django.utils.timezone import now

# Create your models here.

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_desription = models.TextField()

    def __str__(self):
        return self.dep_name




from django.db import models

class Doctors(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctors/', null=True, blank=True)  

    def __str__(self):
        return 'Dr '+ self.name + ' -('+ self.specialization + ')'


class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)


from django.db import models
from django.utils import timezone  

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_on = models.DateTimeField(default=timezone.now)



class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()
    patient_phone = models.CharField(max_length=15)
    appointment_date = models.DateField()
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patient_name} - {self.doctor.name}"

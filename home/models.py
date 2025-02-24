from django.db import models

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
    image = models.ImageField(upload_to='doctors/', null=True, blank=True)  # Allow null and blank
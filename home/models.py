from django.db import models

# Create your models here.

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_desription = models.TextField()

    def __str__(self):
        return self.dep_name


class Doctors(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

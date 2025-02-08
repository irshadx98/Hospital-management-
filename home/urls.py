from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name='index'),
    path('About/', views.About, name='About'),
    path('Booking/', views.Booking, name='Booking'),
    path('Doctors/', views.Doctors, name='Doctors'),
    path('Contact/', views.Contact, name='Contact'),
    path('Department/', views.Department, name='Department'),
]

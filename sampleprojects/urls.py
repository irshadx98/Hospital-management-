from django.contrib import admin
from django.urls import path, include
from home import views  #Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    
    # path('booking/', views.booking_view, name='Booking'),
    # path('doctors/', views.doctors_view, name='Doctors'),
    # path('departments/', views.departments_view, name='Departments'),
    # path('contact/', views.contact_view, name='Contact'),
]

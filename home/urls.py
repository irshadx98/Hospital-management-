from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import book_doctor



# # Define your URL patterns
# from django.urls import path
# from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('About/', views.About, name='About'),
    path('Booking/', views.Booking, name='Booking'),
    path('Doctors/', views.doctors_view, name='Doctors'),  
    path('contact/', views.Contact, name='contact'),
    path('Department/', views.Department, name='Department'),
    path('doctors/', views.doctors_view, name='doctors'),
    path('book_doctor/<int:doctor_id>/', views.book_doctor, name='book_doctor'), 
]
# Add media URL patterns for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     path('contact/', views.Contact, name='contact'), 
# ]    
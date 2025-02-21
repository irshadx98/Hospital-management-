from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('', views.index, name='index'),
    path('About/', views.About, name='About'),
    path('Booking/', views.Booking, name='Booking'),
    path('Doctors/', views.Doctor, name='Doctors'),
    path('Contact/', views.Contact, name='Contact'),
    path('Department/', views.Department, name='Department'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
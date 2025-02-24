from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# # Define your URL patterns
# from django.urls import path
# from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('About/', views.About, name='About'),
    path('Booking/', views.Booking, name='Booking'),
    path('Doctors/', views.doctors_view, name='Doctors'),  # Updated function name
    path('Contact/', views.Contact, name='Contact'),
    path('Department/', views.Department, name='Department'),
]
# Add media URL patterns for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
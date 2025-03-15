from django.contrib import admin

from .models import Departments,Doctors,Booking,Feedback

# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)
class BookingAdmin(admin.ModelAdmin):
    list_display =  ('id', 'p_name', 'p_phone', 'p_email', 'doc_name','booking_date', 'booked_on' )
admin.site.register(Booking,BookingAdmin,)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_on')  
    search_fields = ('name', 'email')
    list_filter = ('submitted_on',)  
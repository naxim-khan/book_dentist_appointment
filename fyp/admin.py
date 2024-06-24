from django.contrib import admin
from .models import DentistRegistration,Appointment,Messages
from django.utils.html import format_html
from django.conf import settings

class DentistRegistrationAdmin(admin.ModelAdmin):
    readonly_fields=['fullName', 'email', 'phone_number', 'date_of_birth', 'specialization', 'fee', 'experience', 'gender', 'address_1', 'address_2',]
    list_display = ('fullName', 'email', 'phone_number', 'date_of_birth', 'specialization', 'fee', 'experience', 'gender', 'address_1', 'address_2','is_approved','profile_image',)
    list_filter = ('is_approved',)
    search_fields = ('fullName', 'email', 'phone_number', 'date_of_birth', 'specialization', 'fee', 'experience', 'gender', 'address_1', 'address_2')
    ordering = ('-id',)  # Orders by date of submission, with most recent first
    
    def rendered_profile_image(self, obj):
        if obj.profile_image:
            image_url = '{}{}'.format(settings.MEDIA_URL, obj.profile_image)
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;">'.format(image_url))
        else:
            return None

    rendered_profile_image.short_description = 'Profile Image'
admin.site.register(DentistRegistration, DentistRegistrationAdmin)

class BookedAppointments(admin.ModelAdmin):
    list_display = ('patient_name', 'patient_email', 'patient_mobile', 'dentist', 'appointment_date', 'problem_description')
    search_fields = ('patient_name', 'patient_email', 'patient_mobile', 'dentist', 'appointment_date', 'problem_description')
    ordering = ('-id',)

    def get_readonly_fields(self, request, obj=None):
        # Define the fields you want to be read-only
        readonly_fields = ['patient_name', 'patient_email', 'patient_mobile', 'dentist', 'appointment_date', 'problem_description']
        return readonly_fields

admin.site.register(Appointment, BookedAppointments)

class MessagesSection(admin.ModelAdmin):
    readonly_fields=['name','email','subject','message']
    list_display = ('name','email','subject','message')
    search_fields = ('name','email','subject','message')
    ordering = ('-id',)

admin.site.register(Messages,MessagesSection)
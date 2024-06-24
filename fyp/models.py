from django.db import models

class DentistRegistration(models.Model):
    profile_image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    fullName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    specialization = models.CharField(max_length=100)
    fee = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)  # Assuming 'male' or 'female'
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200, blank=True)
    # password = models.CharField(max_length=128)  
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return self.fullName


class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()
    patient_mobile = models.CharField(max_length=15)
    dentist = models.CharField(max_length=100)
    appointment_date = models.DateField()
    problem_description = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient_name} with {self.dentist} on {self.appointment_date}"
    
class Messages(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=300)
    message=models.TextField()
    def __str__(self):
        return f"{self.name} | {self.subject} "
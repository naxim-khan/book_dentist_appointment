from django.shortcuts import render,HttpResponse
from .forms import DentistRegistrationForm
from .models import DentistRegistration,Appointment,Messages

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

# Home page
def index(request):
    try:
        if request.method == "POST":
            # Process form data
            patient_name = request.POST.get('patient_name')
            patient_email = request.POST.get('patient_email')
            patient_mobile = request.POST.get('patient_mobile')
            chosen_dentist_name = request.POST.get('dentist')
            appointment_date = request.POST.get('appointment_date')
            problem_description = request.POST.get('problem_description')
            
            try:
                chosen_dentist = DentistRegistration.objects.get(fullName=chosen_dentist_name, is_approved=True)
            except DentistRegistration.DoesNotExist:
                return HttpResponse("Chosen dentist does not exist.", status=400)

            # Send email to the dentist
            dentist_email = chosen_dentist.email
            send_mail(
                'New Appointment Booking',
                f'Appointment Details:\nPatient Name: {patient_name}\nPatient Email: {patient_email}\nAppointment Date: {appointment_date}\nPatient Phone:{patient_mobile}\nProblem Description: {problem_description}',
                'from@example.com',
                [dentist_email],
                fail_silently=False,
            )

            # Render receipt email template
            receipt_email_html = render_to_string('receipt_email.html', {
                'patient_name': patient_name,
                'appointment_date': appointment_date,
                'dentist_name': chosen_dentist.fullName,
                'specialization': chosen_dentist.specialization,
                'experience': chosen_dentist.experience,
                'check_up_fee': chosen_dentist.fee
                # Add more details as needed
            })
            plain_message = strip_tags(receipt_email_html)

            # Send receipt email to the patient
            send_mail(
                'Appointment Receipt',
                plain_message,
                'from@example.com',
                [patient_email],
                html_message=receipt_email_html,
                fail_silently=False,
            )

            appointment = Appointment.objects.create(
                patient_name=patient_name,
                patient_email=patient_email,
                patient_mobile=patient_mobile,
                dentist=chosen_dentist_name,
                appointment_date=appointment_date,
                problem_description=problem_description
            )

            # Redirect to a thank you page or any other page
            return render(request,'thankyou.html')
        approved_dentists = DentistRegistration.objects.filter(is_approved=True)
        return render(request,'index.html',{
            'approved_dentists': approved_dentists
        })
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return HttpResponse(error_message, status=500)

# About Us
def about_us(request):
    try:
        if request.method == "POST":
            # Process form data
            patient_name = request.POST.get('patient_name')
            patient_email = request.POST.get('patient_email')
            patient_mobile = request.POST.get('patient_mobile')
            chosen_dentist_name = request.POST.get('dentist')
            appointment_date = request.POST.get('appointment_date')
            problem_description = request.POST.get('problem_description')
            
            try:
                chosen_dentist = DentistRegistration.objects.get(fullName=chosen_dentist_name, is_approved=True)
            except DentistRegistration.DoesNotExist:
                return HttpResponse("Chosen dentist does not exist.", status=400)

            # Send email to the dentist
            dentist_email = chosen_dentist.email
            send_mail(
                'New Appointment Booking',
                f'Appointment Details:\nPatient Name: {patient_name}\nPatient Email: {patient_email}\nAppointment Date: {appointment_date}\nPatient Phone:{patient_mobile}\nProblem Description: {problem_description}',
                'from@example.com',
                [dentist_email],
                fail_silently=False,
            )

            # Render receipt email template
            receipt_email_html = render_to_string('receipt_email.html', {
                'patient_name': patient_name,
                'appointment_date': appointment_date,
                'dentist_name': chosen_dentist.fullName,
                'specialization': chosen_dentist.specialization,
                'experience': chosen_dentist.experience,
                'check_up_fee': chosen_dentist.fee
                # Add more details as needed
            })
            plain_message = strip_tags(receipt_email_html)

            # Send receipt email to the patient
            send_mail(
                'Appointment Receipt',
                plain_message,
                'from@example.com',
                [patient_email],
                html_message=receipt_email_html,
                fail_silently=False,
            )

            appointment = Appointment.objects.create(
                patient_name=patient_name,
                patient_email=patient_email,
                patient_mobile=patient_mobile,
                dentist=chosen_dentist_name,
                appointment_date=appointment_date,
                problem_description=problem_description
            )
            # Redirect to a thank you page or any other page
            return render(request,"thankyou.html")
        approved_dentists = DentistRegistration.objects.filter(is_approved=True)
        return render(request, 'about.html',{
            'approved_dentists': approved_dentists
        })
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return HttpResponse(error_message, status=500)
    

# Appointment


def appointment(request):
    try:
        if request.method == "POST":
            # Process form data
            patient_name = request.POST.get('patient_name')
            patient_email = request.POST.get('patient_email')
            patient_mobile = request.POST.get('patient_mobile')
            chosen_dentist_name = request.POST.get('dentist')
            appointment_date = request.POST.get('appointment_date')
            problem_description = request.POST.get('problem_description')
            
            try:
                chosen_dentist = DentistRegistration.objects.get(fullName=chosen_dentist_name, is_approved=True)
            except DentistRegistration.DoesNotExist:
                return HttpResponse("Chosen dentist does not exist.", status=400)

            # Send email to the dentist
            dentist_email = chosen_dentist.email
            send_mail(
                'New Appointment Booking',
                f'Appointment Details:\nPatient Name: {patient_name}\nPatient Email: {patient_email}\nAppointment Date: {appointment_date}\nPatient Phone:{patient_mobile}\nProblem Description: {problem_description}',
                'from@example.com',
                [dentist_email],
                fail_silently=False,
            )

            # Render receipt email template
            receipt_email_html = render_to_string('receipt_email.html', {
                'patient_name': patient_name,
                'appointment_date': appointment_date,
                'dentist_name': chosen_dentist.fullName,
                'specialization': chosen_dentist.specialization,
                'experience': chosen_dentist.experience,
                'check_up_fee': chosen_dentist.fee,
                # Add more details as needed
            })
            plain_message = strip_tags(receipt_email_html)

            # Send receipt email to the patient
            send_mail(
                'Appointment Receipt',
                plain_message,
                'from@example.com',
                [patient_email],
                html_message=receipt_email_html,
                fail_silently=False,
            )

            appointment = Appointment.objects.create(
                patient_name=patient_name,
                patient_email=patient_email,
                patient_mobile=patient_mobile,
                dentist=chosen_dentist_name,
                appointment_date=appointment_date,
                problem_description=problem_description
            )

            # Redirect to a thank you page or any other page
            return render(request,'thankyou.html')

        approved_dentists = DentistRegistration.objects.filter(is_approved=True)
        return render(request, 'appointment.html', {
            'approved_dentists': approved_dentists
        })
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return HttpResponse(error_message, status=500)


# Services
def services(request):
    try:
        if request.method == "POST":
            # Process form data
            patient_name = request.POST.get('patient_name')
            patient_email = request.POST.get('patient_email')
            patient_mobile = request.POST.get('patient_mobile')
            chosen_dentist_name = request.POST.get('dentist')
            appointment_date = request.POST.get('appointment_date')
            problem_description = request.POST.get('problem_description')
            
            try:
                chosen_dentist = DentistRegistration.objects.get(fullName=chosen_dentist_name, is_approved=True)
            except DentistRegistration.DoesNotExist:
                return HttpResponse("Chosen dentist does not exist.", status=400)

            # Send email to the dentist
            dentist_email = chosen_dentist.email
            send_mail(
                'New Appointment Booking',
                f'Appointment Details:\nPatient Name: {patient_name}\nPatient Email: {patient_email}\nAppointment Date: {appointment_date}\nPatient Phone:{patient_mobile}\nProblem Description: {problem_description}',
                'from@example.com',
                [dentist_email],
                fail_silently=False,
            )

            # Render receipt email template
            receipt_email_html = render_to_string('receipt_email.html', {
                'patient_name': patient_name,
                'appointment_date': appointment_date,
                'dentist_name': chosen_dentist.fullName,
                'specialization': chosen_dentist.specialization,
                'experience': chosen_dentist.experience,
                'check_up_fee': chosen_dentist.fee
                # Add more details as needed
            })
            plain_message = strip_tags(receipt_email_html)

            # Send receipt email to the patient
            send_mail(
                'Appointment Receipt',
                plain_message,
                'from@example.com',
                [patient_email],
                html_message=receipt_email_html,
                fail_silently=False,
            )

            appointment = Appointment.objects.create(
                patient_name=patient_name,
                patient_email=patient_email,
                patient_mobile=patient_mobile,
                dentist=chosen_dentist_name,
                appointment_date=appointment_date,
                problem_description=problem_description
            )

            # Redirect to a thank you page or any other page
            return render(request,"thankyou.html")
        approved_dentists = DentistRegistration.objects.filter(is_approved=True)
        return render(request, 'service.html',{
            'approved_dentists': approved_dentists
        })
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return HttpResponse(error_message, status=500)

# team
# view.py
from django.http import HttpResponse
from .models import DentistRegistration

from django.http import HttpResponse
from .models import DentistRegistration

from django.http import HttpResponse
from .models import DentistRegistration

def team(request):
    try:
        # Get all approved dentists by default
        approved_dentists = DentistRegistration.objects.filter(is_approved=True)

        if request.method == "POST":
            specialization = request.POST.get('specialization')
            checkup_fee = request.POST.get('checkup_fee')
            experience = request.POST.get('experience')

            # Filter dentists based on selected options
            if specialization and specialization != "Choose Specialization":
                approved_dentists = approved_dentists.filter(specialization=specialization)
            if checkup_fee and checkup_fee != "Choose Fee":
                approved_dentists = approved_dentists.filter(fee=checkup_fee)
            if experience and experience != "Choose Experience":
                approved_dentists = approved_dentists.filter(experience=experience)


            # no_results=False
            # if not approved_dentists.exists():
            #     no_results=True
        no_results = not approved_dentists.exists()
        return render(request, 'team.html', {'approved_dentists': approved_dentists,'error':no_results})

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return HttpResponse(error_message, status=500)

# contact
def contact(request):
    try:
        if request.method == "POST":
            # Process form data
            name = request.POST.get('name')
            email=request.POST.get('email')
            subject=request.POST.get('subject')
            message=request.POST.get('message')
            try:
                # Creating a new Messages object
                Messages.objects.create(
                    name=name,
                    email=email,
                    subject=subject,
                    message=message
                )
                return render(request,'thankyou.html')
            except Exception as e:
                # Handle the exception
                error_message = f"An error occurred: {str(e)}"
                return HttpResponse(error_message, status=500)

        return render(request,'contact.html')
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return HttpResponse(error_message, status=500)

# testimonials
def testimonials(request):
    try:
        return render(request,'testimonial.html')
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return HttpResponse(error_message, status=500)

# features
def features(request):
    try:
        return render(request,'feature.html')
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return HttpResponse(error_message, status=500)

# login/signup

def login_page(request):
    return render(request,'login-page.html')

# Dentist Registration
def dentist_registration(request):
    try:
        if request.method == "POST":
            form = DentistRegistrationForm(request.POST, request.FILES)  # Add request.FILES for handling file uploads

            if form.is_valid():
                profile_image = form.cleaned_data['profile_image']
                full_name = form.cleaned_data['fullName']
                email = form.cleaned_data['email']
                if DentistRegistration.objects.filter(email=email).exists():
                    # If email exists, raise a validation error
                    form.add_error('email', 'This email address is already registered.')
                    return render(request, 'dentist_registration.html', {'form': form})

                phone_number = form.cleaned_data['phone_number']  
                date_of_birth = form.cleaned_data['date_of_birth']  
                specialization = form.cleaned_data['specialization']  
                fee = form.cleaned_data['fee']  
                experience = form.cleaned_data['experience']  
                gender = form.cleaned_data['gender']  
                address_1 = form.cleaned_data['address_1']  
                address_2 = form.cleaned_data.get('address_2', None)  # Optional field
                # password = form.cleaned_data['password']  

                # Creating a new instance of the model
                dentist_registration = DentistRegistration.objects.create(
                    profile_image=profile_image,
                    fullName=full_name,
                    email=email,
                    phone_number=phone_number,
                    date_of_birth=date_of_birth,
                    specialization=specialization,
                    fee=fee,
                    experience=experience,
                    gender=gender,
                    address_1=address_1,
                    address_2=address_2,
                    # password=password
                )

                # Reset the form for a new registration
                form = DentistRegistrationForm()
                return render(request, 'thankyou.html',)
        else:
            form = DentistRegistrationForm()

        approved_dentists = DentistRegistration.objects.filter(is_approved=True)
        return render(request, 'dentist_registration.html', {'form': form})
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return HttpResponse(error_message, status=500)

def compress_image(image):
    img = Image.open(image)
    output = BytesIO()
    # Resize the image to a smaller size
    img.thumbnail((300, 300))
    # Save the resized image to the BytesIO buffer
    img.save(output, format='JPEG', quality=60)
    # Create an InMemoryUploadedFile from the BytesIO buffer
    output.seek(0)
    return InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)


def handler404(request, exception):
    return render(request, '404.html', status=404)
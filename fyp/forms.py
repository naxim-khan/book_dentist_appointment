# # forms.py
# from django import forms


from django import forms
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

SPECIALIZATIONS_CHOICES = [
    ('', 'Choose Specialization'),
    ('Orthodontics', 'Orthodontics'),
    ('Oral and Maxillofacial surgery', 'Oral and Maxillofacial surgery'),
    ('Periodontology', 'Periodontology'),
    ('Endodontics', 'Endodontics'),
    ('Oral Medicine and Radiology', 'Oral Medicine and Radiology'),
    ('Prosthodontics', 'Prosthodontics'),]

FEE_CHOICES = [
    ('', 'Choose Fee'),
    ('300', 'Rs. 300'),
    ('500', 'Rs. 500'),
    ('600', 'Rs. 600'),
]

EXPERIENCE_CHOICES = [
    ('', 'Years of experience'),
    ('1-3', '1 to 3 years'),
    ('3-5', '3 to 5 years'),
    ('5+', '5+ years'),
]

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]

class DentistRegistrationForm(forms.Form):
    profile_image = forms.ImageField(
        label="Update image",
        required=False,
        widget=forms.FileInput(attrs={'id': 'input-file'})
    )
    fullName = forms.CharField(label="Full Name:", max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Enter Full name'}))
    email = forms.EmailField(label="Email", max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
    phone_number = forms.IntegerField(label="Phone Number",widget=forms.NumberInput(attrs={'placeholder': 'Enter Phone Number'}))
    date_of_birth=forms.DateField(label="Date of Birth",widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'type': 'date'}))
    specialization = forms.ChoiceField(label="Specialization", choices=SPECIALIZATIONS_CHOICES, required=True, widget=forms.Select(attrs={'id': 'specialization', 'required': 'required'}))
    fee = forms.ChoiceField(label="Checkup Fee", choices=FEE_CHOICES, required=True, widget=forms.Select(attrs={'id': 'fee', 'required': 'required'}))
    experience = forms.ChoiceField(label="Experience", choices=EXPERIENCE_CHOICES, required=True, widget=forms.Select(attrs={'id': 'experience', 'required': 'required'}))
    gender = forms.ChoiceField(label="Gender", choices=GENDER_CHOICES, widget=forms.RadioSelect)
    address_1 = forms.CharField(label="Address:", max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Street Address'}))
    address_2 = forms.CharField( required=False, label="Address:", max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Address line 2 optional'}))
    # password = forms.CharField(label="Enter Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    is_approved = forms.BooleanField(label="Approval Status", initial=False, required=False)

    # def clean_password(self):
    #     password = self.cleaned_data.get("password")
    #     if len(password) < 8:
    #         raise forms.ValidationError("Password must be at least 8 characters long.")
    #     return make_password(password)

    def clean(self):
        cleaned_data = super(DentistRegistrationForm, self).clean()
        # password = cleaned_data.get("password")
        # Hash the password before saving
        # cleaned_data['password'] = make_password(password)
        return cleaned_data


from django import forms

from . models import *  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User   
        fields =("username","password1","password2")
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"

class AmbulanceForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = "__all__"
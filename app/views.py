from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from . forms import *
from . models import *
from django.http import HttpResponse
from . forms import SignUpForm

def Home(request):
    return render(request,"home.html")

def Appointment(request):
    if request.method=="POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request,f'Ambulance will arrive soon.')
            return redirect("Appointment_Confirm")

    else:
        form = AppointmentForm()
    return render(request,"appointment.html",{"form":form})


def Appointment_Confirm(request):
    return render(request,"Appointment_confirm.html")

def Request_Abmulance(request):
    if request.method=="POST":
        form = AmbulanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Reach_Ambulance")
            # messages.success(request,"done")
    else:
        form = AmbulanceForm()
    return render(request,"ambulance.html",{"form":form  })


def Reach_Ambulance(request):
    return render(request,"Reach_Ambulance.html")

def SignUp(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Home")
    else:
        form = SignUpForm()
    return render(request,"signup.html",{"form":form})

def doc_info(request):
    return render(request,"doc_info.html")

def Contact_us(request):
    return render(request,"Contact_us.html")
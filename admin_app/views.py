from django.shortcuts import render,redirect
from app.models import Ambulance
from app.models import Appointment
# Create your views here.
from . forms import *
from django.contrib import messages

# Create your views here.
def Admin_Home(request):
    return render(request,"admin.html")

def Add_Doctor(request):
    if request.method=="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"New Doctor Added.!")

            return redirect("Add_Doctor_Done")
    else:
        form = Form()
    return render(request,"doctor.html",{"form":form})


def Add_Doctor_Done(request):
    return render(request,"Add_Doctor_Done.html")

def Read_Doctor(request):
    read=Doctor.objects.all()
    return render(request,"Read_Doctor.html",{"read":read})

def Update_Doctor(request,id):
    upd=Doctor.objects.get(id=id)
    update = DoctorForm(request.POST or None,request.FILES or None,instance=upd)
    if update.is_valid():
        update.save()
        return redirect("Read_Doctor")

    return render(request,"Update_Doctor.html",{"update":update})

def Delete_Doctor(request,id):
    del_t=Doctor.objects.get(id=id)    
    
    # if request.method =="POST": 
        # delete object 
    del_t.delete() 
        # after deleting redirect to  
        # home page 
    return redirect("Read_Doctor") 


def Read_Appointment(request):
    read=Appointment.objects.all()
    return render(request,"Read_Appointment.html",{"read":read}) 

def Add_Nurse(request):
    if request.method=="POST":
        form = NurseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"New Nurse Added.!")

            return redirect("Add_Nurse_Done")
    else:
        form = NurseForm()
    return render(request,"Nurse.html",{"form":form})

def Add_Nurse_Done(request):
    return render(request,"Add_Nurse_Done.html")

def Read_Nurse(request):
    read=Nurse.objects.all()
    return render(request,"Read_Nurse.html",{"read":read})

def Update_Nurse(request,id):
    upd=Nurse.objects.get(id=id)
    update = NurseForm(request.POST or None,request.FILES or None,instance=upd)
    if update.is_valid():
        update.save()
        return redirect("Read_Nurse")
    return render(request,"Update_Nurse.html",{"update":update})

def Delete_Nurse(request,id):
    del_t=Nurse.objects.get(id=id)    
    
    # if request.method =="POST": 
        # delete object 
    del_t.delete() 
        # after deleting redirect to  
        # home page 
    return redirect("Read_Nurse") 
  
    # return render(request, "Delete_Nurse.html") 


def Read_Ambulance(request):
    read=Ambulance.objects.all()
    return render(request,"Read_Ambulance.html",{"read":read})   
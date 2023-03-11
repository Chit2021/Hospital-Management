from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("",views.Admin_Home,name="Admin_Home"),

    path("Add_Doctor/",views.Add_Doctor,name="Add_Doctor"),
    path("Add_Doctor_Done/",views.Add_Doctor_Done,name="Add_Doctor_Done"),
    path("Read_Doctor/",views.Read_Doctor,name="Read_Doctor"),
    path("Update_Doctor/<int:id>",views.Update_Doctor,name="Update_Doctor"),
    path("Delete_Doctor/<int:id>",views.Delete_Doctor,name="Delete_Doctor"),

    path("Read_Appointment/",views.Read_Appointment,name="Read_Appointment"),

    path("Add_Nurse/",views.Add_Nurse,name="Add_Nurse"),
    path("Add_Nurse_Done/",views.Add_Nurse_Done,name="Add_Nurse_Done"),
    path("Read_Nurse/",views.Read_Nurse,name="Read_Nurse"),
    path("Update_Nurse/<int:id>",views.Update_Nurse,name="Update_Nurse"),
    path("Delete_Nurse/<int:id>",views.Delete_Nurse,name="Delete_Nurse"),

    path("Read_Ambulance/",views.Read_Ambulance,name="Read_Ambulance"),

]
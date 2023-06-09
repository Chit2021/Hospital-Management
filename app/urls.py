from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.Home,name="Home"),
    path("appointment/",views.Appointment,name="appointment"),
    path("Appointment_Confirm/",views.Appointment_Confirm,name="Appointment_Confirm"),
    
    path("SignUp/",views.SignUp,name="SignUp"),
    path("doc_info/",views.doc_info,name="doc_info"),

    path("Request_Abmulance/",views.Request_Abmulance,name="Request_Abmulance"),
    path("Reach_Ambulance/",views.Reach_Ambulance,name="Reach_Ambulance"),
    path("Contact_us/",views.Contact_us,name="Contact_us"),
]
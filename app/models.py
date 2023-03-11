from django.db import models

# Create your models here.

class Appointment(models.Model):
    
    Patient_Name = models.CharField(max_length=40)
    Patient_Age = models.IntegerField()
    Patient_Contact = models.IntegerField()
    Location = models.CharField(max_length=30)
    # Reason = models.ForeignKey(Disease,on_delete=models.CASCADE)

    def __str__(self):
        return self.Patient_Name

class Ambulance(models.Model):
    Patient_Name = models.CharField(max_length=30)
    # Patient_Age = models.IntegerField()
    # Patient_Contact = models.IntegerField()
    Location = models.CharField(max_length=20)
    # Disease = models.ForeignKey(Reason,on_delete=models.CASCADE)

    def __str__(self):
        return self.Patient_Name

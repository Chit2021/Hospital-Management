from django.db import models

# Create your models here.

class Speciality(models.Model):
    speciality = models.CharField(max_length=30)

    def __str__(self):
        return self.speciality

class Doctor(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Specialist = models.ForeignKey(Speciality,on_delete=models.CASCADE)
    Experience = models.IntegerField()

class Shift(models.Model):
    shift = models.CharField(max_length=20)
    def __str__(self):
        return self.shift

class Nurse(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Department = models.CharField(max_length=20)
    Shift = models.ForeignKey(Shift,on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class Gender(models.Model):
    gender = models.CharField(max_length=10)
    def __str__(self):
        return self.gender


class Room_Service(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Gender = models.ForeignKey(Gender,on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=40)

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    ATACQ = models.ForeignKey(
        Car, 
        on_delete=models.CASCADE,
        related_name='Vehicle')
    
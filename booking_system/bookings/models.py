# bookings/models.py
from django.db import models

class Flat(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='bookings')
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self):
        return f"{self.flat.name}: {self.checkin} - {self.checkout}"

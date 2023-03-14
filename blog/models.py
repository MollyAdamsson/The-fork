from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.PositiveIntegerField()
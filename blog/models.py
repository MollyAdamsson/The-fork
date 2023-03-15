from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Booking made"))


class Booking(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.PositiveIntegerField()

    class Meta:
        ordering = ["-created_on"]
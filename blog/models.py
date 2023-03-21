from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator


STATUS = ((0, "Busy"), (1, "Booking made"))


class Booking(models.Model):
    """ Model to create a booking """
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(default=datetime.now())
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    userId = models.CharField(max_length=50, null=True)
    num_guests = models.IntegerField(validators=[MinValueValidator(1)])

    def clean_date(self):
        date = self.cleaned_data['date']
        today = datetime.now().date()
        if date < today:
            raise forms.ValidationError
            ('Invalid - cannot book in the past')
        if date > today + timedelta(weeks=4):
            raise forms.ValidationError
            ('Invalid - bookings can only be made up to 4 weeks in advance')
        return date

    def clean_time(self):
        time = self.cleaned_data['time']
        date = self.cleaned_data['date']
        datetime_obj = datetime.combine(
            date, datetime.strptime(time, '%H:%M').time())
        if datetime_obj < datetime.now():
            raise forms.ValidationError('Invalid - cannot book in the past')
        if datetime_obj > datetime.now() + timedelta(minutes=30):
            raise forms.ValidationError(
                'bookings can only be made 30 mins in advance'
                )
        return time

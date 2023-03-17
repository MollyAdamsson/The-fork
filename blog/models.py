from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator


STATUS = ((0, "Busy"), (1, "Booking made"))


class Booking(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField()
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.IntegerField(validators=[MinValueValidator(1)])

    def clean_date(self):
        date = self.cleaned_data['date']
        today = datetime.now().date()
        if date < today:
            raise forms.ValidationError('Invalid date - cannot book in the past')
        if date > today + timedelta(weeks=4):
            raise forms.ValidationError('Invalid date - bookings can only be made up to 4 weeks in advance')
        return date

    def clean_time(self):
        time = self.cleaned_data['time']
        date = self.cleaned_data['date']
        datetime_obj = datetime.combine(date, datetime.strptime(time, '%H:%M').time())
        if datetime_obj < datetime.now():
            raise forms.ValidationError('Invalid time - cannot book in the past')
        return time
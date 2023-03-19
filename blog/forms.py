from django import forms
from datetime import datetime, timedelta
from .models import Booking
from crispy_forms.helper import FormHelper


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date', 'time', 'num_guests']
        booking_date = forms.DateField(help_text="Date must be a future date")
        widgets = {
            'name': forms.TextInput
            (attrs={'class': 'forms-control', 'placeholder': 'name'}),
            'date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'}),
            'time': forms.TimeInput(
                format=('%H:%M'),
                attrs={'class': 'form-control', 'placeholder': 'Choose Time', 'type': 'time'}),
                }


class BookingFormStaff(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date', 'time', 'num_guests', 'userId']
        booking_date = forms.DateField(help_text="Date must be a future date")
        widgets = {
            'name': forms.TextInput
            (attrs={'class': 'forms-control', 'placeholder': 'name'}),
            'date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'}),
            'time': forms.TimeInput(
                format=('%H:%M'),
                attrs={'class': 'form-control', 'placeholder': 'Choose Time', 'type': 'time'}),
                }
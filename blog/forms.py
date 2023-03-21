from django import forms
from datetime import datetime, timedelta
from .models import Booking
from crispy_forms.helper import FormHelper


class BookingForm(forms.ModelForm):
    """
    Form to create and edit a booking
    """
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date', 'time', 'num_guests']
        booking_date = forms.DateField(help_text="Date must be a future date")
        widgets = {
            'name': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'name'}),
            'email': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'email'}),
            'date': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'}),
            'time': forms.TimeInput(
                format=('%H:%M'),
                attrs={'class': 'form-control', 'placeholder': 'Choose Time',
                                'type': 'time'}
            ),
            'num_guests': forms.TextInput(
                attrs={'class': 'form-control'}),
                }


class BookingFormStaff(forms.ModelForm):
    """
    Form to create and edit a booking for staff
    """
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date', 'time', 'num_guests', 'userId']
        booking_date = forms.DateField(help_text="Date must be a future date")
        widgets = {
            'name': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'name'}),
            'email': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'email'}),
            'date': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'}),
            'time': forms.TimeInput(
                format=('%H:%M'),
                attrs={'class': 'form-control', 'placeholder': 'Choose Time',
                                'type': 'time'}
            ),
            'num_guests': forms.TextInput(
                attrs={'class': 'form-control'}),
            'userId': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'userId'}),
                }

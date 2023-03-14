from django.shortcuts import render, redirect
from .forms import BookingForm


def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)

# Create your views here.

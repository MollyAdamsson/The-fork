from django.shortcuts import render, redirect
from django.views import generic
from .forms import BookingForm
from .models import Booking


def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
        else:
            form = BookingForm()
    return render(request, 'book_table.html', {'form': form})


def booking_success(request):
    return render(request, 'booking_sucess.html')
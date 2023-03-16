from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import TemplateView
from .forms import BookingForm
from .models import Booking


class IndexView(TemplateView):
    template_name = '../templates/index.html'


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
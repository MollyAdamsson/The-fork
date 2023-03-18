from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views import generic
from django.views.generic import TemplateView
from django.views import View
from .forms import BookingForm
from .models import Booking


class IndexView(TemplateView):
    template_name = 'index.html'


class MenuView(TemplateView):
    template_name = 'menu.html'


class CreateBookingView(View):
    template_name = 'create_booking.html'

    def get(self, request):
        form = BookingForm()
        return render(request, 'create_booking.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        model = Booking
        form = BookingForm(request.POST)
        Booking_made = False
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            date = request.POST['date']
            time = request.POST['time']
            num_guests = request.POST['num_guests']
            errorMessage = None
        return render(request, 'create_booking.html', {'form': form})
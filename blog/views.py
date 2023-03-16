from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import TemplateView
from django.views import View
from .forms import BookingForm
from .models import Booking


class IndexView(TemplateView):
    template_name = 'index.html'


def login(request):
    return render(request, 'login.html', context=None)


def signUp(request):
    return render(request, 'Sign-up.html', context=None)


def loggedin(request):
    return render(request, 'logged-in.html', context=None)


def manage_booking(request):
    return render(request, 'manage_booking.html', context=None)


def view_booking(request):
    return render(request, 'view_booking.html', context=None)


class CreateBookingView(View):

    def get(self, request, *args, **kwargs):
        form = BookingForm()
        return render(request, 'create_booking.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
        return render(request, 'create_booking.html', {'form': form})
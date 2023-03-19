from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views import generic
from django.views.generic import TemplateView
from django.views import View
from .forms import BookingForm, BookingFormStaff
from .models import Booking


class IndexView(TemplateView):
    template_name = 'index.html'


class MenuView(TemplateView):
    template_name = 'menu.html'


class CreateBookingView(View):
    template_name = 'create_booking.html'

    def get(self, request):
        if request.user.is_superuser or request.user.is_staff:
            form = BookingFormStaff()
        else:
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
            userId = request.user.id
            errorMessage = None
            bookings = Booking.objects.filter(time=time, date=date)

            if bookings.count() <= 0:
                newBooking = Booking(name=name, email=email, date=date,
                    time=time, num_guests=num_guests, userId=userId)
                newBooking.save()
                
        return render(request, 'create_booking.html', {'form': form})


class ManageBookingView(TemplateView):
    template_name = 'manage_booking.html'

    def get(self, request):
        if request.user.is_staff:
            bookings = Booking.objects.all()
        else:
            bookings = Booking.objects.filter(userId=request.user.id)

        return render(request, 'manage_booking.html', context={'object_list': bookings})


class DeleteBookingView(TemplateView):
    template_name = 'delete_booking.html'

    def get(self, request):
        id = self.request.GET.get('bookingId')
        booking = Booking.objects.filter(pk=id)
        
        if booking.count() > 0 and (request.user.is_staff or str(request.user.id) == booking[0].userId):
            booking.delete()
            return render(request, 'delete_success.html', context={'success': True})
        else:
            return render(request, 'delete_success.html', context={'success': False})


class EditBookingView(TemplateView):
    template_name = 'edit_booking.html'

    def get(self, request):
        id = self.request.GET.get('bookingId')
        booking = Booking.objects.get(pk=id)
        
        if booking is not None and (request.user.is_staff or str(request.user.id) == booking.userId):
            form = BookingForm(request.POST or None, instance=booking)
            return render(request, 'edit_booking.html', context={'form': form, 'showForm': True})
        else:
            return render(request, 'edit_booking.html', context={'showForm': False})

    def post(self, request, *args, **kwargs):
        model = Booking
        booking = Booking.objects.get(pk=id)
        form = BookingForm(request.POST)
        Booking_made = False
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            date = request.POST['date']
            time = request.POST['time']
            num_guests = request.POST['num_guests']
            errorMessage = None

            booking.name = name
            booking.email = email
            booking.date = date
            booking.time = time
            booking.num_guests = num_guests

            booking.save()

            return render(request, 'edit_booking.html')


class BookingSuccessView(TemplateView):
    template_name = 'booking_success.html'


class DeleteSuccessView(TemplateView):
    template_name = 'delete_success.html'


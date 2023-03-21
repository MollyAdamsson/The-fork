from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views import View
from .forms import BookingForm, BookingFormStaff
from .models import Booking
from django.views.generic.edit import UpdateView


class IndexView(TemplateView):
    """
    View to the home page
    """
    template_name = 'index.html'


class MenuView(TemplateView):
    """
    View to the menu page
    """

    template_name = 'menu.html'


class CreateBookingView(View):
    """
    View to render createbookings
    and allow user to create a booking
    """
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
                newBooking = Booking(
                    name=name, email=email, date=date, time=time,
                    num_guests=num_guests, userId=userId
                    )
                newBooking.save()
                Booking_made = True
                return render(
                    request, 'booking_success.html',
                    {
                        'Booking_made': Booking_made}
                    )
            else:
                errorMessage = "Sorry, this time slot has already been taken."
                return render(
                    request, 'create_booking.html',
                    {
                        'form': form,
                        'errorMessage': errorMessage
                    }
                )

        return render(request, 'create_booking.html', {'form': form})


class ManageBookingView(ListView):
    """
    View to render ManageBookings
    """
    model = Booking
    template_name = 'manage_booking.html'

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.model.objects.all()
        else:
            return self.model.objects.filter(userId=self.request.user.id)


class DeleteBookingView(TemplateView):
    """ A view to delete a booking """
    template_name = 'delete_booking.html'

    def get(self, request):
        id = self.request.GET.get('bookingId')
        booking = Booking.objects.filter(pk=id)

        if booking.count() > 0 and (
            request.user.is_staff or str(request.user.id) == booking[0].userId
                    ):
            booking.delete()
            return render(
                request, 'delete_success.html', context={'success': True}
                )
        else:
            return render(
                request, 'delete_success.html', context={'success': False}
                )


class EditBookingView(UpdateView):
    """
    A view to provide a Form to the user
    to edit a booking
    """
    model = Booking
    template_name = 'edit_booking.html'
    form_class = BookingForm
    success_url = '/managebooking'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.object.userId == str(
            self.request.user.id
                ) or self.request.user.is_staff:
            context['showForm'] = True
        return context


class BookingSuccessView(TemplateView):
    """
    A view to show the booking was successfull
    """
    template_name = 'booking_success.html'


class DeleteSuccessView(TemplateView):
    """
    A view to provide the user with a delete sucess page
    """
    template_name = 'delete_success.html'

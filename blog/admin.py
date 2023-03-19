from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('name', 'name')
    search_fields = ['name', 'content']
    summernote_fields = ('content')

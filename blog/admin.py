from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug')
    search_fields = ['name', 'content']
    list_filter = ('created_on', 'updated_on')
    summernote_fields = ('content')

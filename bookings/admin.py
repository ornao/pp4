from django.contrib import admin
from .models import Bookings


@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    """ a class for bookings admin """
    list_display = (
        'booking_id', 'user', 'created_date', 'last_name', 'length_of_stay')
    search_fields = ['check_in_date', 'check_out_date']
    list_filter = ('created_date', 'last_name')

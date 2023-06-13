from django.contrib import admin
from .models import Bookings

@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_date', 'last_name', 'length_of_stay')
    search_fields = ['check_in_date', 'check_out_date']
    list_filter = ('created_date', 'last_name')

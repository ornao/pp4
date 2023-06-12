from django.shortcuts import render
from django.views import generic
from .models import Bookings


class BookingsList(generic.ListView):
    model = Bookings
    template_name = "read_bookings.html"


class BookingsCreate(generic.CreateView):
    model = Bookings
    template_name = "create_bookings.html"
    fields = "first_name", "last_name", "email", "check_in_date", "check_out_date"
    

# need to add booking successful page and url 
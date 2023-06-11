from django.shortcuts import render
from django.views import generic
from .models import Bookings


class BookingsList(generic.ListView):
    model = Bookings
    template_name = "bookings.html"

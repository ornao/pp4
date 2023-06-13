from django.shortcuts import render
from django.views import generic
from .models import Bookings
from django.urls import reverse, reverse_lazy


class BookingsList(generic.ListView):
    model = Bookings
    template_name = "read_bookings.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Bookings.objects.filter(user=self.request.user).order_by('-created_date')
        else:
            return Bookings.objects.none()



class BookingsCreate(generic.CreateView):
    model = Bookings
    template_name = "create_bookings.html"
    fields = "first_name", "last_name", "email", "check_in_date", "check_out_date"
    success_url = reverse_lazy("read_bookings")

    def form_valid(self, form):
        """assigns logged-in user to user field in database"""
        form.instance.user = self.request.user  
        return super().form_valid(form)

# need to add booking successful page and url 
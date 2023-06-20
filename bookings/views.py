from django.shortcuts import render
from django.views import generic
from .models import Bookings
from django.urls import reverse, reverse_lazy
from bookings.forms import BookingsForm
from django.contrib.messages.views import SuccessMessageMixin


class BookingsList(generic.ListView):
    model = Bookings
    template_name = "read_bookings.html"

    # restrict bookings so only logged in user can see their own bookings
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Bookings.objects.filter(user=self.request.user).order_by('-created_date')
        else:
            return Bookings.objects.none()



class BookingsCreate(SuccessMessageMixin, generic.CreateView):
    model = Bookings
    template_name = "create_bookings.html"
    fields = "first_name", "last_name", "email", "check_in_date", "check_out_date", "num_guests", "accomodation_name", 
    success_url = reverse_lazy("read_bookings")
    success_message = "Booking was created successfully"

    def form_valid(self, form):
        """assigns logged-in user to user field in database"""
        form.instance.user = self.request.user  
        return super().form_valid(form)


class BookingsEdit(generic.UpdateView):
    model = Bookings
    form_class = BookingsForm
    template_name = 'edit_bookings.html'
    success_url = reverse_lazy('read_bookings') 


class BookingsDelete(generic.DeleteView):
    model = Bookings
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy("read_bookings")


# need to add booking successful message (unique url?)
# can probably delete need to add first name and surname to booking maybe just a display instead? as shpuld have from login info
# update template of bookings to make more realistic 
# begin to work on edit and delete functionality
# check if see can use lets go hydro accomodation and make app and table accordingly

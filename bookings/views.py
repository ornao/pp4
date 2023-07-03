from django.shortcuts import render
from django.views import generic
from .models import Bookings
from django.urls import reverse, reverse_lazy
from bookings.forms import BookingsForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


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
    form_class = BookingsForm
    success_url = reverse_lazy('read_bookings') 
    success_message = "Booking was created successfully"

    def form_valid(self, form):
        """assigns logged-in user to user field in database"""
        form.instance.user = self.request.user  
        return super().form_valid(form)


class BookingsEdit(SuccessMessageMixin, generic.UpdateView):
    model = Bookings
    form_class = BookingsForm
    template_name = 'edit_bookings.html'
    success_url = reverse_lazy('read_bookings') 
    success_message = "Booking was edited successfully"


class BookingsDelete(generic.DeleteView):
    model = Bookings
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy("read_bookings")
    success_message = "Booking was deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BookingsDelete, self).delete(request, *args, **kwargs)


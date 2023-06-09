from django.shortcuts import render
from django.views import generic
from .models import Bookings
from django.urls import reverse, reverse_lazy
from bookings.forms import BookingsForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.template import RequestContext


class BookingsList(generic.ListView):
    """ a class for bookings read """
    model = Bookings
    template_name = "read_bookings.html"

    # restrict bookings so only logged in user can see their own bookings
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Bookings.objects.filter(
                user=self.request.user).order_by('-created_date')
        else:
            return Bookings.objects.none()


class BookingsCreate(SuccessMessageMixin, generic.CreateView):
    """ a class for creating bookings """
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
    """ a class for editing bookings """
    model = Bookings
    form_class = BookingsForm
    template_name = 'edit_bookings.html'
    success_url = reverse_lazy('read_bookings')
    success_message = "Booking was edited successfully"


class BookingsDelete(generic.DeleteView):
    """ a class for deleting bookings """
    model = Bookings
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy("read_bookings")
    success_message = "Booking was deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BookingsDelete, self).delete(request, *args, **kwargs)


# error handling found on slack without need for url, /
# adapted to include 403 and 400 error and work on /
# this version of django (Django==3.2.19)

def handler404(request, *args, **argv):
    """ handles 404 error """
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    """ handles 500 error """
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


def handler403(request, *args, **argv):
    """ handles 403 error """
    response = render_to_response('403.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 403
    return response


def handler400(request, *args, **argv):
    """ handles 400 error """
    response = render_to_response('400.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 400
    return response

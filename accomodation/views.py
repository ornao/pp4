from django.shortcuts import render
from django.views import generic
from .models import Accomodation


class AccomodationList(generic.ListView):
    """
    a class for the Accomodation view
    """
    model = Accomodation
    template_name = "accomodation.html"

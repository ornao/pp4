from django.shortcuts import render
from django.views import generic
from .models import Accomodation


class AccomodationList(generic.ListView):
    model = Accomodation
    # queryset = Accomodation.objects.filter(status=1).order_by('availibility')
    # template_name = "accomodation.html"

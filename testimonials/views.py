from django.shortcuts import render
from django.views import generic
from .models import Testimonials


class TestimonialsList(generic.ListView):
    model = Testimonials()
    queryset = Testimonials().objects.filter(status=1).order_by('date_created')
    template_name = "index.html"

from django.shortcuts import render
from django.views import generic
from .models import Testimonials


class TestimonialsList(generic.ListView):
    """ a class for testimonials view """
    model = Testimonials
    queryset = Testimonials.objects.filter(status=1).order_by('-created_date')
    template_name = "testimonials.html"

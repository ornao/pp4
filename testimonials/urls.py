from . import views
from django.urls import path

urlpatterns = [
    path("", views.TestimonialsList.as_view(), name="testimonials"),
]
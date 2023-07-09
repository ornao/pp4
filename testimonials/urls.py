from . import views
from django.urls import path

# renders view to user
urlpatterns = [
    path("", views.TestimonialsList.as_view(), name="testimonials"),
]

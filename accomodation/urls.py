from . import views
from django.urls import path

urlpatterns = [
    path("", views.AccomodationList.as_view(), name="accomodation"),
]
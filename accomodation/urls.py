from . import views
from django.urls import path

#  allows view to be rendered to user
urlpatterns = [
    path("", views.AccomodationList.as_view(), name="accomodation"),
]

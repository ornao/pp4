from . import views
from django.urls import path

urlpatterns = [
    path("", views.BookingsList.as_view(), name="read_bookings"),
    path("create/", views.BookingsCreate.as_view(), name="create_bookings"),
    path("edit/", views.BookingsEdit.as_view(), name="edit_bookings"),
    
]
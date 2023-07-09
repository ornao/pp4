from . import views
from django.urls import path

# allows views to be rendered to user
urlpatterns = [
    path("", views.BookingsList.as_view(), name="read_bookings"),
    path("create/", views.BookingsCreate.as_view(), name="create_bookings"),
    path("edit/<int:pk>/", views.BookingsEdit.as_view(), name="edit_bookings"),
    path(
        "delete/<int:pk>/",
        views.BookingsDelete.as_view(), name="delete_bookings"),
]

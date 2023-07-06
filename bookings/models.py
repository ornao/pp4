from django.db import models
from django.contrib.auth.models import User
from accomodation.models import Accomodation

# Booking model for the database


class Bookings(models.Model):
    """
    a class for the Booking model
    """
    booking_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(
        max_length=254,
        default=""
        )
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    accomodation_name = models.ForeignKey(
        Accomodation, on_delete=models.CASCADE, related_name='name', null=True)
    num_guests = models.IntegerField(null=True)

    @property
    def length_of_stay(self):
        return self.check_out_date - self.check_in_date

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.booking_id

from django.db import models
from django.contrib.auth.models import User

# Booking model for the database

class Booking(models.Model):
    """
    a class for the Booking model
    """
    booking_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    length_of_stay = models.DurationField()
    num_guests = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    num_guests = models.IntegerField()
    price_per_night = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    accomodation_id = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=50,
        null=True
        )
    email = models.EmailField(
        max_length=254,
        default=""
        )

    # class Meta:
        
    # # def __str__(self):
    # #     return self.
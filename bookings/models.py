from django.db import models
from django.contrib.auth.models import User

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

    @property
    def length_of_stay(self):
        return self.check_out_date - self.check_in_date

  
    # num_guests = models.IntegerField()
    
    # price_per_night = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    # total_price = models.DecimalField(max_digits=10, decimal_places=2)
    # accomodation_id = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
   

    class Meta:
        ordering = ['created_date']
        
    # # def __str__(self):
    # #     return self.
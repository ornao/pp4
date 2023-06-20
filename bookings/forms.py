from .models import Bookings
from django import forms

# class BookingsForm(forms.Form):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     email = forms.EmailField()
#     check_in_date = forms.DateField()

class BookingsForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ("first_name", "last_name", "email", "check_in_date", "check_out_date", "num_guests", "accomodation_name", "price_per_night",)
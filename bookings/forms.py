from .models import Bookings
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingsForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ("first_name", "last_name", "email", "check_in_date", "check_out_date", "num_guests", "accomodation_name",)
        widgets = {
            'check_in_date': DateInput(),
            'check_out_date': DateInput(),
        }
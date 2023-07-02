from .models import Bookings
from django import forms
from django.core.exceptions import ValidationError

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingsForm(forms.ModelForm):
    # django documentation form validation
    def clean(self):
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get("check_in_date")
        check_out_date = cleaned_data.get("check_out_date")
        num_guests = cleaned_data.get("num_guests")
        accomodation_name = cleaned_data.get("accomodation_name")

        if check_in_date and check_out_date:
            if check_in_date > check_out_date:   
                raise ValidationError("Check-in date cannot be after check-out date")

        if num_guests and accomodation_name:
            if num_guests >= 3 and accomodation_name not in ['pod cupla', 'honeymoon pod']:
                raise ValidationError("This pod will not allow for more than 2 guests")

    class Meta:
        model = Bookings
        fields = ("first_name", "last_name", "email", "check_in_date", "check_out_date", "num_guests", "accomodation_name",)
        widgets = {
            'check_in_date': DateInput(),
            'check_out_date': DateInput(),
        }
from .models import Bookings
from django import forms
from django.core.exceptions import ValidationError

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingsForm(forms.ModelForm):
    # django documentation
    def clean(self):
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get("check_in_date")
        check_out_date = cleaned_data.get("check_out_date")

        if check_in_date and check_out_date:
            # Only do something if both fields are valid so far.
            if check_in_date > check_out_date:
                raise ValidationError(
                    "Check in date cannot be after check date!"
                )

    class Meta:
        model = Bookings
        fields = ("first_name", "last_name", "email", "check_in_date", "check_out_date", "num_guests", "accomodation_name",)
        widgets = {
            'check_in_date': DateInput(),
            'check_out_date': DateInput(),
        }
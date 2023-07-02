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

        if num_guests:
            if num_guests > 6:
                raise ValidationError("6 guests is the maximum any of our available pods or cabins will accomodate")


        if num_guests and accomodation_name:
            if num_guests == 6 and accomodation_name not in ['Family Cabin']:
                self.add_error(None, "Too many guests for pod selected")
            elif num_guests == 2 and accomodation_name not in ['Honeymoon Pod','Pod Cupla']:
                self.add_error(None, "Honeymoon Pod or Pod Cupla are fantastic options - we strongly recommend those instead for 2 guests") 
            elif num_guests == 1 and accomodation_name not in ['Honeymoon Pod','Pod Cupla']:
                self.add_error(None, "Honeymoon Pod or Pod Cupla are fantastic options - we strongly recommend those instead for 1 guest")
            elif num_guests == 3 and accomodation_name not in ['Family Cabin', 'Teach Papa Rua', 'Pod Almighty']:
                self.add_error(None, "This pod only accomodates maximum two guests")
            elif num_guests == 4 and accomodation_name not in ['Teach Papa Rua']:
                self.add_error(None, "Teach Papa Rua is a fantastic option for 4 people - we strongly recommend this pod instead") 
            elif num_guests == 5 and accomodation_name not in ['Pod Almighty']:
                self.add_error(None, "Pod Almighty is a fantastic option for 5 people - we strongly recommend this pod instead") 

    class Meta:
        model = Bookings
        fields = ("first_name", "last_name", "email", "check_in_date", "check_out_date", "num_guests", "accomodation_name",)
        widgets = {
            'check_in_date': DateInput(),
            'check_out_date': DateInput(),
        }
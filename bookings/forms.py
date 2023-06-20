from django import forms 

class BookingsForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    check_in_date = forms.DateField()
    check_out_date = forms.DateField()

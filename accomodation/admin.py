from django.contrib import admin
from .models import Accommodation
from django_summernote.admin import SummernoteModelAdmin

# decorator to allow more than two arguements
@admin.register(Accommodation)
class AccommodationAdmin(SummernoteModelAdmin):

    list_display = ('accomodation_name', 'availibility')
    search_fields = ['accomodation_name']
    list_filter = ('availibility', 'capacity')
    summernote_fields = ('description',)

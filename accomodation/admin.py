from django.contrib import admin
from .models import Accomodation
from django_summernote.admin import SummernoteModelAdmin

# decorator to allow more than two arguements
@admin.register(Accomodation)
class AccomodationAdmin(SummernoteModelAdmin):

    list_display = ('accomodation_name', 'availibility')
    search_fields = ['accomodation_name']
    list_filter = ('availibility', 'capacity')
    summernote_fields = ('description',)

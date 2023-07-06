from django.contrib import admin
from .models import Testimonials
from django_summernote.admin import SummernoteModelAdmin


# decorator to allow more than two arguements
@admin.register(Testimonials)
class TestimonialsAdmin(SummernoteModelAdmin):

    list_display = ('rating', 'status', 'created_date')
    search_fields = ['rating']
    list_filter = ('status', 'created_date')
    summernote_fields = ('content',)

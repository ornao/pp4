from django.contrib import admin
from .models import Testimonials
from django_summernote.admin import SummernoteModelAdmin

# decorator to allow more than two arguements
@admin.register(Testimonials)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

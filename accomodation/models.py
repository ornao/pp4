from django.db import models
from cloudinary.models import CloudinaryField

class Accomodation(models.Model):
    """
    a class for the Accomodation model
    """
    accomodation_id = models.AutoField(primary_key=True)
    accomodation_name = models.CharField(
        max_length=50,
        unique=True
        )
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=5, decimal_places=2)
    accomodation_type = models.CharField(max_length=50)
    availibility = models.BooleanField(default=False)

    # class Meta:
    #     ordering = ['-']

    def __str__(self):
        return self.accomodation_name

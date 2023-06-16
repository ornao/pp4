from django.db import models

class Accommodation(models.Model):
    """
    a class for the Accomodation model
    """
    accomodation_id = models.AutoField(primary_key=True)
    accomodation_name = models.CharField(
        max_length=50,
        unique=True
        )
    description = models.TextField()
    capacity = models.IntegerField()
    price_per_night = models.FloatField()
    accomodation_type = models.IntegerField()
    availability = models.BooleanField(default=False)

    # class Meta:
    #     ordering = ['-']

    def __str__(self):
        return self.accomodation_name

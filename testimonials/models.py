from django.db import models
from django.contrib.auth.models import User
from accomodation.models import Accomodation
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator

STATUS = ((0, "Draft"), (1, "Published"))


class Testimonials(models.Model):
    """ a class for testimonials model """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_testimonials"
    )
    # add max and min possible inputs
    rating = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
            ])
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    accomodation_name = models.ForeignKey(
        Accomodation, on_delete=models.CASCADE,
        related_name="user_accomodation", null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    # for future iterations
    likes = models.ManyToManyField(
        User, related_name='testimonial_likes', blank=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.content

    # for future iterations
    def number_of_likes(self):
        return self.likes.count()

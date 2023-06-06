from django.db import models
from django.contrib.auth.models import User



STATUS = ((0, "Draft"), (1, "Published"))


class Testimonials(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_testimonials"
    )
    rating = models.IntegerField()
    content = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='testimonial_likes', blank=True)
    
    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.rating

    def number_of_likes(self):
        return self.likes.count()



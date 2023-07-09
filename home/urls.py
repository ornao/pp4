from . import views
from django.urls import path

# allows views to be rendered to user
urlpatterns = [
    path("", views.home, name="home"),
]

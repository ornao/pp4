from django.shortcuts import render


def home(request):
    """
    a function to display the homepage
    """
    return render(request, 'index.html')

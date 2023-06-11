from django.shortcuts import render

# Displays the home page


def home(request):
    """
    a view to display the homepage
    """
    return render(request, 'index.html')

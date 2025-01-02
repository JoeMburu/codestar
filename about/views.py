from django.shortcuts import render

from about.models import About

# Create your views here.

def about_me(request):
    """
    Renders the About page.
    """
    about = About.objects.all().order_by('-updated_on').first()
    return render(
        request, 
        'about/about.html', 
        { "about": about },
)

from django.shortcuts import render
from . import  models

def home(request, short_link=None, *args, **kwargs):
    """home - show home page"""
    if short_link:
        pass
    else:
        return render(
            request,
            'home.html',
        )



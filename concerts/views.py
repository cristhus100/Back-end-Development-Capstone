from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Concert


def index(request):
    """Home page showing band information"""
    context = {
        'band_name': 'The Python Rockers',
        'tagline': 'Bringing code to life through music',
        'description': 'We are a group of developer-musicians who love creating awesome music and even more awesome code. Join us on our journey!',
    }
    return render(request, 'concerts/index.html', context)


def concert_list(request):
    """List all concerts"""
    concerts = Concert.objects.all().order_by('event_date')
    return render(request, 'concerts/concert_list.html', {'concerts': concerts})

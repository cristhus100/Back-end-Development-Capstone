from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Photo


def photo_list(request):
    """List all photos"""
    photos = Photo.objects.all()
    return render(request, 'photos/photo_list.html', {'photos': photos})

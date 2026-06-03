from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Song


def song_list(request):
    """List all songs"""
    songs = Song.objects.all()
    return render(request, 'songs_app/song_list.html', {'songs': songs})

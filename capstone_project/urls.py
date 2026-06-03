from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('concerts.urls')),
    path('songs/', include('songs_app.urls')),
    path('photos/', include('photos.urls')),
]

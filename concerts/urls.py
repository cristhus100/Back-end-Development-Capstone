from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('concerts/', views.concert_list, name='concert_list'),
]

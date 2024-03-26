from django.urls import path
from . import views

urlpatterns = [
    path('coin/<int:amount_flips>/', views.coin, name='coin'),
    path('dice/', views.dice, name='dice'),
    path('number/', views.number, name='number'),
]

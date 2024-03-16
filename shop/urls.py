from django.urls import path
from .views import index, user_orders

urlpatterns = [
    path('', index, name='index'),
    path('user/<int:user_id>/<str:period>/', user_orders, name='user_orders'),
]

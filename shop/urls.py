from django.urls import path
from .views import index, edit_product, data_saved

urlpatterns = [
    path('', index, name='index'),
    path('edit_product/<int:product_id>/', edit_product, name='edit_product'),
    path('data_saved/', data_saved, name='data_saved'),
]
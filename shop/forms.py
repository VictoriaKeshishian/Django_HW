from django import forms
from datetime import datetime


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    amount = forms.IntegerField()
    image = forms.ImageField(required=False)




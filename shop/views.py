from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm


def index(request):
    return render(request, 'home.html')


def data_saved(request):
    return render(request, 'shop/data_saved.html')


def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.amount = form.cleaned_data['amount']
            if 'image' in request.FILES:
                product.image = request.FILES['image']
            product.save()
            messages.success(request, 'Данные о товаре успешно сохранены')
            return redirect('data_saved')
    else:
        form = ProductForm(initial={'name': product.name, 'description': product.description, 'price': product.price, 'amount': product.amount})
    return render(request, 'shop/edit_product.html', {'form': form})
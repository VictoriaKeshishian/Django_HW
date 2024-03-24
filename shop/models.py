from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    date_registration = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return (f'Username: {self.name}, email: {self.email}, number: {self.number}, address: {self.address}, '
                f'date_registration: {self.date_registration}')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField()
    date_add_product = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

from django.core.management.base import BaseCommand
from shop.models import User


class Command(BaseCommand):
    help = "Add new user."

    def handle(self, *args, **kwargs):
        user = User(name='Anna', email='anna@example.com', number='79005558866', address='st.Gogolya 2', password='secret2')
        user.save()
        self.stdout.write(f'{user}')

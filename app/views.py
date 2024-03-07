from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request):
    username = "User123"
    current_date = datetime.now()
    return render(request, 'index.html', {'username': username, 'current_date': current_date})


def about(request):
    return render(request, 'about.html')



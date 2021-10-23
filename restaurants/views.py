from django.shortcuts import render, get_object_or_404
from .models import Restaurant, History
from datetime import datetime


def home_page(request):
    restaurants = Restaurant.objects
    data = {
        'restaurants': restaurants,
        'date_today': datetime.today().date()
    }
    return render(request, 'restaurants/home.html', data)


def history_page(request):
    history = History.objects
    data = {'history': history}
    return render(request, 'restaurants/history.html', data)

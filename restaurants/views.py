from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, History, Vote, Setting
from django.contrib.auth.models import User
from datetime import datetime
from decimal import Decimal
from . import forms
import ast


def index(request):
    restaurants = Restaurant.objects.order_by('name')
    total_votes, show_message = check_user_can_vote(request.user.id)
    data = {
        'restaurants': restaurants,
        'date_today': datetime.today().date(),
        'user': request.user.username,
        'message_can_vote': show_message,
        'votes': total_votes
    }
    return render(request, 'restaurants/index.html', data)


def history(request):
    history_data = History.objects
    if not history_data:
        return redirect('/')
    data = {
        'history': history_data,
        'date_today': datetime.today().date(),
    }
    return render(request, 'restaurants/history.html', data)


def get_configurable_votes():
    try:
        configurable_vote = Setting.objects.filter(name='votes_per_day')[:1]
        value = 0
        if configurable_vote:
            check_value = ast.literal_eval(configurable_vote[0].value)
            if isinstance(check_value, int):
                value = check_value
        return value
    except Exception as error:
        pass


def check_user_can_vote(user_id):
    config_value = get_configurable_votes()
    default_votes_per_day = Restaurant.votes_per_day
    votes_per_day = config_value or default_votes_per_day
    all_votes = len(Vote.objects.filter(user=user_id))
    total = votes_per_day - all_votes
    return (total, True) if all_votes < votes_per_day else (total, False)


def vote_form(request, restaurant_id):
    if request.method == 'POST':
        if restaurant_id and request.user:
            try:
                restaurant = Restaurant.objects.get(id=restaurant_id)
                votes = len(Vote.objects.filter(user=request.user.id, restaurant=restaurant_id))
                can_vote = check_user_can_vote(request.user.id)[1]
                if can_vote:
                    Vote.objects.create(
                        restaurant=restaurant,
                        user=request.user,
                        date=datetime.today().replace(microsecond=0)
                    )
                    votes += 1
                    vote_amount = 0.25
                    if votes == 1:
                        vote_amount = 1
                    elif votes == 2:
                        vote_amount = 0.5

                    restaurant.vote_amount += Decimal(vote_amount)
                    restaurant.save(update_fields=['vote_amount'])

            except Exception as error:
                print("Error: %s", error)

    return redirect('/')

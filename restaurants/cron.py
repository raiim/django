
from django.db.models import Max
from .models import Restaurant, History, Vote
from datetime import datetime


def history_cron_job():
    print("\n--------\nCRON Job\n--------\n")
    # get_history_data()


def get_history_data():
    max_vote_amount = Restaurant.objects.aggregate(Max('vote_amount')).get('vote_amount__max')
    if not max_vote_amount:
        return

    restaurants = Restaurant.objects.filter(vote_amount=max_vote_amount)
    if len(restaurants) > 1:
        data = {}
        for restaurant in restaurants:
            votes = Vote.objects.filter(restaurant=restaurant.id).order_by('-date')
            users = len(list(dict.fromkeys([rec.user.id for rec in votes])))
            max_date = max([rec.date for rec in votes])
            if data.get("users", 0) < users or data.get("users", 0) == users and data.get("date") < max_date:
                data.update({
                    "restaurant": restaurant.id,
                    "users": users,
                    "date": max_date
                })
        if data:
            restaurants = [rec for rec in restaurants if rec.id == data.get('restaurant')][0]
            create_history(restaurants)
    else:
        create_history(restaurants)


def create_history(restaurant):
    exist = History.objects.filter(date=datetime.today().date())
    if not exist:
        History.objects.create(
            name=restaurant.name,
            vote_amount=restaurant.vote_amount,
            date=datetime.today().replace(microsecond=0)
        )
        Restaurant.objects.update(vote_amount=0.00)
        Vote.objects.all().delete()

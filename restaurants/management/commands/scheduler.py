from django.core.management.base import BaseCommand
from apscheduler.schedulers.blocking import BlockingScheduler
from restaurants.models import Restaurant, History, Vote
from django.db.models import Max
from datetime import datetime


class Command(BaseCommand):
    help = 'Creates Restaurant group with permissions {add, change, view, delete}'

    def handle(self, *args, **options):
        self.stdout.write("Works!")
        sched = BlockingScheduler()

        @sched.scheduled_job('interval', minutes=3)
        def timed_job():
            print('This job is run every three minutes.')

        @sched.scheduled_job('cron', hour=0)
        def scheduled_job():
            print('This job is run every day')

            max_vote_amount = Restaurant.objects.aggregate(Max('vote_amount')).get('vote_amount__max')
            if not max_vote_amount:
                return

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

            restaurants = Restaurant.objects.filter(vote_amount=max_vote_amount)
            if len(restaurants) > 1:
                data = {}
                for record in restaurants:
                    votes = Vote.objects.filter(restaurant=record.id).order_by('-date')
                    users = len(list(dict.fromkeys([rec.user.id for rec in votes])))
                    max_date = max([rec.date for rec in votes])
                    if data.get("users", 0) < users or data.get("users", 0) == users and data.get("date") < max_date:
                        data.update({
                            "restaurant": record.id,
                            "users": users,
                            "date": max_date
                        })
                if data:
                    restaurants = [rec for rec in restaurants if rec.id == data.get('restaurant')][0]
                    create_history(restaurants)
            else:
                create_history(restaurants)

        sched.start()
        print("Scheduler started")

        while __name__ == '__main__':
            pass

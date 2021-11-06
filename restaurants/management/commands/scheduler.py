from django.core.management.base import BaseCommand
from apscheduler.schedulers.blocking import BlockingScheduler
from restaurants.models import Restaurant, History, Vote
from django.db.models import Max
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Creates Restaurant group with permissions {add, change, view, delete}'

    def handle(self, *args, **options):
        self.stdout.write("Works!")
        sched = BlockingScheduler()

        # next_day = datetime.today().replace(microsecond=0, hour=0, minute=0, second=0) + timedelta(days=1)
        #
        # @sched.scheduled_job('interval', days=1, start_date=next_day)
        # def timed_job():
        #     print('This job is run every every day at midnight')
        #     self._create_history_records()

        @sched.scheduled_job('cron', day_of_week='mon-sun', hour=13, minute=20)
        def scheduled_job():
            print('This job is run one time')
            self._create_history_records()

        sched.start()

        while __name__ == '__main__':
            pass

    def _create_history_records(self):
        max_vote_amount = Restaurant.objects.aggregate(Max('vote_amount')).get('vote_amount__max')
        if not max_vote_amount:
            return

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
                self._create_history(restaurants)
        else:
            self._create_history(restaurants[0])

    def _create_history(self, restaurant):
        check_date = datetime.now().date() - timedelta(days=1)
        exist = History.objects.filter(date=check_date)
        if not exist:
            History.objects.create(
                name=restaurant.name,
                vote_amount=restaurant.vote_amount,
                date=check_date
            )
            Restaurant.objects.update(vote_amount=0.00)
            Vote.objects.all().delete()

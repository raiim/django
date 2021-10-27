from apscheduler.schedulers.blocking import BlockingScheduler
from django.db.models import Max
from .models import Restaurant, History, Vote
from datetime import datetime

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three minutes.')


# @sched.scheduled_job('cron', hour=0)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')
#     get_history_data()


sched.start()
print("Scheduler started")

while __name__ == '__main__':
  pass


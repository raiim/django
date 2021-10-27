web: python manage.py loaddata settings
web: python manage.py add_group
web: python manage.py crontab add
web: python manage.py runserver 0.0.0.0:$PORT
release: python manage.py migrate
clock: python heroku_cron.py
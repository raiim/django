# Restaurant Vote app

Terminal
 - generate SECRET_KEY if needed 
 - python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

create file django/environment.json
 - { "SECRET_KEY": "..." }

Docker
 - install docker app
 - docker-compose build
 - docker-compose up
 - docker exec -it django_vote_container bash
   - python manage.py crontab add
   
   Create Admin User (execute one time for fresh start)
   - python manage.py createsuperuser
   

Configurable votes:
 - Login, go to admin site
 - Select Table - Settings
 - add number of votes per restaurant into value of votes_per_day
 - default is 0 (hardcoded votes is 5)
   - output will be: total_votes = (votes_per_day or hardcoded) * (len(restaurants) or 1)

 

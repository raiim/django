# Restaurant Vote app

Docker
 - add file environment.json
   - { "SECRET_KEY": "..." }
 - docker-compose build
 - docker-compose up
 - docker exec -it django_vote_container bash
 - python manage.py crontab add

Configurable votes:
 - Select Table - Settings
 - add number of votes per restaurant into value of votes_per_day
 - default is 0 (hardcoded votes is 5)
   - ex. 5 votes * len(restaurants) or 1
 
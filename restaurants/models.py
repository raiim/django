from django.db import models


# Create your models here.
class Restaurant(models.Model):
    votes_per_day = 20
    name = models.CharField(max_length=20)
    summary = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    vote_amount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, editable=False)

    def __str__(self):
        return self.name


class History(models.Model):
    name = models.CharField(max_length=20)
    summary = models.CharField(max_length=200, blank=True)
    vote_amount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    published_date = models.DateTimeField('Date published')

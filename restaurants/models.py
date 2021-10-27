from django.db import models
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
import os


@receiver(models.signals.post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created and instance.is_active and not instance.is_superuser:
        """On create User add permission to log in Admin site and add Restaurant Group by default"""
        if not instance.groups.filter(name='Restaurant Group').exists():
            try:
                restaurant_group = Group.objects.get(name='Restaurant Group')
                settings_group = Group.objects.get(name='Settings Group')
            except Group.DoesNotExist:
                pass
            else:
                instance.is_staff = True
                instance.groups.add(restaurant_group)
                instance.groups.add(settings_group)
                instance.save()


# Create your models here.
def content_file_name(instance, filename):
    ext = filename.split('.')
    filename = "image_%s.%s" % (instance.id or ext[0], ext[-1])
    return os.path.join('images', filename)


class Restaurant(models.Model):
    votes_per_day = 5
    name = models.CharField(max_length=20)
    summary = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to=content_file_name, blank=True)
    vote_amount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, editable=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique restaurant')
        ]

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


class History(models.Model):
    name = models.CharField(max_length=20)
    vote_amount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    date = models.DateField(null=True)

    class Meta:
        verbose_name_plural = 'History'

    def __str__(self):
        return self.name


class Vote(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()


class Setting(models.Model):
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=200)
    note = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Settings'

    def __str__(self):
        return self.name

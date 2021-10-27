from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Creates Custom groups'

    def handle(self, *args, **options):
        restaurant_group, created = Group.objects.get_or_create(name='Restaurant Group')
        settings_group, created = Group.objects.get_or_create(name='Settings Group')

        add_restaurant = Permission.objects.get(codename='add_restaurant')
        change_restaurant = Permission.objects.get(codename='change_restaurant')
        delete_restaurant = Permission.objects.get(codename='delete_restaurant')
        view_restaurant = Permission.objects.get(codename='view_restaurant')
        change_settings = Permission.objects.get(codename='change_setting')
        view_settings = Permission.objects.get(codename='view_setting')

        restaurant_group.permissions.add(
            add_restaurant,
            change_restaurant,
            delete_restaurant,
            view_restaurant
        )
        settings_group.permissions.add(
            change_settings,
            view_settings
        )

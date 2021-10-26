from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Creates Restaurant group with permissions {add, change, view, delete}'

    def handle(self, *args, **options):
        # self.stdout.write("Works!")
        restaurant_group, created = Group.objects.get_or_create(name='Restaurant Group')

        add_restaurant = Permission.objects.get(codename='add_restaurant')
        change_restaurant = Permission.objects.get(codename='change_restaurant')
        delete_restaurant = Permission.objects.get(codename='delete_restaurant')
        view_restaurant = Permission.objects.get(codename='view_restaurant')

        restaurant_group.permissions.add(add_restaurant, change_restaurant, delete_restaurant, view_restaurant)
        # print("Created Restaurant group and permissions.")

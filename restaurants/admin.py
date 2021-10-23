from django.contrib import admin
from .models import Restaurant

# Register your models here.
admin.site.register(Restaurant)


class RestaurantAdmin(admin.ModelAdmin):
    readonly_fields = ('vote_amount',)

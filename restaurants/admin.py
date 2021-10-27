from django.contrib import admin
from .models import Restaurant, Setting


# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    readonly_fields = ('vote_amount',)
    list_display = ('name', 'vote_amount')


admin.site.register(Restaurant, RestaurantAdmin)


class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'note')


admin.site.register(Setting, SettingAdmin)

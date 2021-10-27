from django.contrib import admin
from .models import Restaurant, Setting, History


# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    readonly_fields = ('vote_amount',)
    list_display = ('name', 'vote_amount')
    exclude = ('image',)


admin.site.register(Restaurant, RestaurantAdmin)


class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'note')


admin.site.register(Setting, SettingAdmin)


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'vote_amount')
    readonly_fields = ('name', 'date', 'vote_amount')

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(History, HistoryAdmin)


from django.contrib import admin

from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('number', 'date',)
    list_filter = ('number', 'date',)
    empty_value_display = '-empty-'


admin.site.register(Application, ApplicationAdmin)

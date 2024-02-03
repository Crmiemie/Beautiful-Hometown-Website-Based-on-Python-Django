from django.contrib import admin

from govern.models import News, Last_update

# Register your models here.
admin.site.register(News)
admin.site.register(Last_update)
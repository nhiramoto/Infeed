from django.contrib import admin

from .models import List, Source, Item

admin.site.register(List)
admin.site.register(Source)
admin.site.register(Item)

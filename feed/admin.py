from django.contrib import admin

from .models import SourceList, Source, SourceItem

admin.site.register(SourceList)
admin.site.register(Source)
admin.site.register(SourceItem)

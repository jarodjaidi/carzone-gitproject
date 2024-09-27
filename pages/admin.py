from django.contrib import admin
from django.utils.html import format_html
from .models import Team

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50%">'.format(object.photo.url))
    list_display = ('id','thumbnail','first_name', 'last_name', 'designation', 'created_at')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'designation')
    list_per_page = 10

admin.site.register(Team, TeamAdmin)


from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Profile)


@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish')
    list_filter = ('author', 'created_at', 'updated_at', )
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', 'body',)}
    date_hierarchy = 'publish'
    ordering = ('publish',)



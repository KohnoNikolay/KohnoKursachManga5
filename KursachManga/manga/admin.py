from django.contrib import admin
from .models import *


class TitlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'slug', 'poster', 'chapters')
    list_display_links = ('id', 'name', )
    search_fields = ('name', 'author', )
    prepopulated_fields = {"slug": ("name", )}


class ChaptersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'images')
    list_display_links = ('id', 'name', )
    search_fields = ('name',)


admin.site.register(Titles, TitlesAdmin)
admin.site.register(Images)
admin.site.register(Chapters, ChaptersAdmin)

# Register your models here.

from django.contrib import admin

# Register your models here.

from . models import Word, League

class LeagueAdminConfig(admin.ModelAdmin):
    model = League
    search_fields = ('id', 'language', 'name', )
    list_filter =('language', 'name', )
    list_display = ('id', 'language', 'name', )

class WordAdminConfig(admin.ModelAdmin):
    model = Word
    search_fields = ('id', 'language', 'word',)
    list_filter =('language',)
    list_display = ('id', 'language','word',)
admin.site.register(Word, WordAdminConfig)
admin.site.register(League, LeagueAdminConfig)
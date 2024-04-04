from django.contrib import admin
from apps.team.models import Team, Founder

# Register your models here.

class TeamFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'descriptions')
    search_fields = ('name', 'descriptions')
    
class FounderFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'descriptions')
    search_fields = ('name', 'descriptions')
       
admin.site.register(Team, TeamFilterAdmin)
admin.site.register(Founder, FounderFilterAdmin)
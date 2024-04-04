from django.contrib import admin
from apps.contact import models

# Register your models here.

class ContactFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

    
class ReservFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'number')
    search_fields = ('name', 'number')
    
admin.site.register(models.Contacts, ReservFilterAdmin)
admin.site.register(models.PageContact, ContactFilterAdmin)


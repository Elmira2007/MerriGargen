from django.contrib import admin
from apps.settings import models

# Register your models here.
class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    
class ServicesFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')  
      
class SlideFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    
class VideoFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)
    
    
admin.site.register(models.Video, VideoFilterAdmin)   
admin.site.register(models.Slide, SlideFilterAdmin)    
admin.site.register(models.Settings, SettingsFilterAdmin)
admin.site.register(models.Services, ServicesFilterAdmin)
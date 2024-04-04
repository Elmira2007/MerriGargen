from django.contrib import admin
from apps.secondary import models

# Register your models here.
class AboutFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    
class NewsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    
class ListFilterAdmin(admin.ModelAdmin):
    list_filter = ('image_1', )
    list_display = ('image_1', 'image_2')
    search_fields = ('image_1', 'image_2')
    
class GalleryFilterAdmin(admin.ModelAdmin):
    list_filter = ('image', )
    list_display = ('image',)
    search_fields = ('image',)
    
admin.site.register(models.News, NewsFilterAdmin)
admin.site.register(models.About, AboutFilterAdmin)
admin.site.register(models.Gallery, GalleryFilterAdmin)
admin.site.register(models.List, ListFilterAdmin)
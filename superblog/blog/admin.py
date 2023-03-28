from django.contrib.admin.decorators import register
from django.contrib import admin
from .models import Photo, Blog


@register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image', 'caption')
    list_filter = ('caption', )
    search_fields = ['caption']
    prepopulated_fields = {'image': ('caption',)}


@register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_created')
    list_filter = ('title', )
    search_fields = ['title', 'content']
    prepopulated_fields = {'title': ('title',)}

from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name', 'description')


class PageArticlesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'article', 'pub_date', 'image', 'category')
    search_fields = ('name', 'description', 'article')

admin.site.register(Category, CategoryAdmin)
admin.site.register(PageArticles, PageArticlesAdmin)

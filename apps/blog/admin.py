from django.contrib import admin
from .models import Category, Blog
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['author', 'topic', 'click_nums', 'add_time', 'modify_time', 'tag']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)

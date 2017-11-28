from django.contrib import admin
from django.db import models
# from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget
from .models import Category, Blog, Article, Tag, Comment
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    """
    name = models.CharField(max_length=20, verbose_name=u"类别名")
    """
    list_display = ['name']


class BlogAdmin(admin.ModelAdmin):
    """
    author = models.ForeignKey(UserProfile, verbose_name=u"作者", null=True, blank=True)
    topic = models.CharField(max_length=100, verbose_name=u"博客名")
    content = models.TextField(verbose_name="简介")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    """
    list_display = ['author', 'topic', 'add_time']


class ArticleAdmin(admin.ModelAdmin):
    """
    topic = models.CharField(max_length=100, verbose_name=u"标题")
    content = models.TextField(verbose_name="内容")
    tag = models.CharField(max_length=20, verbose_name=u"标签")
    category = models.ForeignKey(Category, verbose_name=u"类别", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    modify_time = models.DateTimeField(default=datetime.now, verbose_name=u"修改时间")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    """
    list_display = ['topic', 'get_all_tags_name', 'category', 'add_time', 'modify_time', 'click_nums']


class TagAdmin(admin.ModelAdmin):
    """
    name = models.CharField(max_length=20, verbose_name=u"标签")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    """
    list_display = ['name', 'add_time']


class CommentAdmin(admin.ModelAdmin):
    """
    user = models.ForeignKey(UserProfile, verbose_name=u"作者", null=True, blank=True)
    article = models.ForeignKey(Article, verbose_name=u"文章", null=True, blank=True)
    content = models.TextField(verbose_name="评论内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    """
    list_display = ['user', 'article', 'add_time']

# class MyModelAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.TextField: {'widget': AdminMarkdownxWidget},
#     }


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
# admin.site.register(MyModel, MyModelAdmin)

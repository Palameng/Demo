from django.db import models
from datetime import datetime
from users.models import UserProfile
from markdownx.models import MarkdownxField
# Create your models here.


class Category(models.Model):
    """
    类别
    """
    name = models.CharField(max_length=20, verbose_name=u"类别名")

    class Meta:
        verbose_name = u"类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_all_follow_article_nums(self):
        return self.article_set.count()


class Blog(models.Model):
    """
    博客
    """
    author = models.ForeignKey(UserProfile, verbose_name=u"作者", null=True, blank=True)
    topic = models.CharField(max_length=100, verbose_name=u"博客名")
    content = models.TextField(verbose_name="简介")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"博客"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.topic


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"标签")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"文章标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    blog = models.ForeignKey(Blog, verbose_name=u"所属博客", null=True, blank=True)
    topic = models.CharField(max_length=100, verbose_name=u"标题")
    content = models.TextField(verbose_name="内容")
    tags = models.ManyToManyField(Tag, verbose_name="标签")
    category = models.ForeignKey(Category, verbose_name=u"类别", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    modify_time = models.DateTimeField(default=datetime.now, verbose_name=u"修改时间")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")

    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.topic

    def get_all_tags_name(self):
        return "\n".join([tag.name for tag in self.tags.all()])


class MyModel(models.Model):
    test = MarkdownxField()

    class Meta:
        verbose_name = u"Markdown测试"
        verbose_name_plural = verbose_name

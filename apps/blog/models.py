from django.db import models
from datetime import datetime
from users.models import UserProfile
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


class Article(models.Model):
    blog = models.ForeignKey(Blog, verbose_name=u"所属博客", null=True, blank=True)
    topic = models.CharField(max_length=100, verbose_name=u"标题")
    content = models.TextField(verbose_name="内容")
    tag = models.CharField(max_length=20, verbose_name=u"标签")
    category = models.ForeignKey(Category, verbose_name=u"类别", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    modify_time = models.DateTimeField(default=datetime.now, verbose_name=u"修改时间")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")

    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.topic

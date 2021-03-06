# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 20:30
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('tag', models.CharField(max_length=20, verbose_name='标签')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='类别')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.RemoveField(
            model_name='blog',
            name='click_nums',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='modify_time',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='tag',
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='topic',
            field=models.CharField(max_length=100, verbose_name='博客名'),
        ),
    ]

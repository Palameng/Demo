# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 18:13
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_mymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=markdownx.models.MarkdownxField(verbose_name='内容'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 20:24
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100)),
                ('Content', DjangoUeditor.models.UEditorField(verbose_name='内容')),
            ],
        ),
    ]

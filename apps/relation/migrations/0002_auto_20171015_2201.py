# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 22:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='部门名称')),
            ],
        ),
        migrations.AddField(
            model_name='staffs',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='relation.Departments', verbose_name='部门名称'),
        ),
    ]

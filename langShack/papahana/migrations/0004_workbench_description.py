# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-21 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papahana', '0003_auto_20180120_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='workbench',
            name='description',
            field=models.TextField(default='d'),
        ),
    ]
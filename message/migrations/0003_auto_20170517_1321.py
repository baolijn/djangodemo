# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20170517_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='object_id',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False, verbose_name='\u4e3b\u952e'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_auto_20160504_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='record_locked',
            field=models.BooleanField(default=False, help_text='Not presently implemented or used'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='version',
            field=models.PositiveIntegerField(default=0, help_text='Internal tracking version number'),
        ),
    ]
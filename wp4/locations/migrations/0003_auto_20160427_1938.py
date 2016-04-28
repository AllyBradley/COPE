# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20160201_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Not presently used/implemented. For legacy data when a location closes for use', verbose_name='HO03 is active'),
        ),
    ]

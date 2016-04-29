# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0007_auto_20160120_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='not_randomised_because',
            field=models.PositiveSmallIntegerField(choices=[(0, 'DOc15 Not Applicable'), (1, 'DOc10 Donor not proceeding'), (2, 'DOc11 One or more kidneys allocated to non-trial location'), (3, 'DOc12 Kidneys not allocated'), (4, 'DOc13 Kidneys not transplanable'), (5, 'DOc14 Other')], default=0, verbose_name='DO51 Why was this not randomised?'),
        ),
    ]
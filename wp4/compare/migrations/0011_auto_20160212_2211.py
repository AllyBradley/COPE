# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-12 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0010_auto_20160202_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donor',
            old_name='form_completed',
            new_name='procurement_form_completed',
        ),
        migrations.RemoveField(
            model_name='organ',
            name='allocated',
        ),
        migrations.RemoveField(
            model_name='recipient',
            name='form_completed',
        ),
        migrations.AddField(
            model_name='organ',
            name='transplantation_form_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organ',
            name='transplantation_notes',
            field=models.TextField(blank=True, verbose_name='DO51 Transplantation notes'),
        ),
    ]
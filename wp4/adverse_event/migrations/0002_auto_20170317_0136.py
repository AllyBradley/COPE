# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 01:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compare', '0001_initial'),
        ('adverse_event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='contact',
            field=models.ForeignKey(help_text='AEh09 This should be the Local Investigator for the Transplant Centre', on_delete=django.db.models.deletion.CASCADE, related_name='adverse_event_contact', to=settings.AUTH_USER_MODEL, verbose_name='AE09 primary contact'),
        ),
        migrations.AddField(
            model_name='event',
            name='organ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compare.Organ', verbose_name='AE04 trial id link'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='event',
            order_with_respect_to='organ',
        ),
    ]
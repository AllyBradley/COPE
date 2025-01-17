# Generated by Django 2.2 on 2019-05-03 09:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0010_donor_hypertension'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='panel_reactive_antibodies',
            field=models.PositiveSmallIntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='DO54 panel reactive antibodies'),
        ),
        migrations.AddField(
            model_name='donor',
            name='panel_reactive_antibodies_unknown',
            field=models.BooleanField(default=False, help_text='Internal unknown flag'),
        ),
    ]

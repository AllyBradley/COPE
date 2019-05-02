# Generated by Django 2.2 on 2019-05-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0009_auto_20190222_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='hypertension',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(2, 'MMc03 Unknown'), (0, 'MMc01 No'), (1, 'MMc02 Yes')], default=None, null=True, verbose_name='DO53 donor hypertension'),
        ),
    ]

# Generated by Django 2.2 on 2019-05-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0011_auto_20190503_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='organ',
            name='actual_treatment_received',
            field=models.PositiveSmallIntegerField(choices=[(0, 'ORc931 HMP O2'), (1, 'ORc932 HMP'), (2, 'ORc933 Cold Storage'), (3, 'ORc934 Unknown'), (4, 'ORc934 No Treatment')], default=3, verbose_name='OR93 actual treatment received'),
        ),
        migrations.AddField(
            model_name='organ',
            name='intention_to_treat',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(3, 'MMc04 Not Applicable'), (0, 'MMc01 No'), (1, 'MMc02 Yes')], default=None, null=True, verbose_name='OR94 intention to treat'),
        ),
    ]

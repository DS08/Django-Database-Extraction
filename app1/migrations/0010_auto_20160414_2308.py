# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-14 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_auto_20160414_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='eligibility',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='procedure',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-14 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='amount_in_rupees',
            field=models.IntegerField(),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 12:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20170817_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operations',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 8, 17, 12, 23, 15, 714904, tzinfo=utc)),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-16 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0024_speedup'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='SpeedUp',
            field=models.ManyToManyField(to='major.SpeedUp'),
        ),
    ]

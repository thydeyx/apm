# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-09 08:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0059_auto_20161009_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobinfo',
            name='runmodule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='major.RunModule'),
        ),
    ]

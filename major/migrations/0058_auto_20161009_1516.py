# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-09 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0057_auto_20161009_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='runmodule',
            name='modulename',
            field=models.CharField(max_length=255),
        ),
    ]
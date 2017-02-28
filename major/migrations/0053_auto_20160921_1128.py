# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-21 03:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0052_tasks_regression_jobstream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='regression_jobstream',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='major.JobStream'),
        ),
    ]

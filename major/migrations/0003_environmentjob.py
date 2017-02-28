# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-13 01:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0002_auto_20160713_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvironmentJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='major.Environment')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='major.JobStream')),
            ],
        ),
    ]

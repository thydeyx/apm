# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-16 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0019_auto_20160809_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeedConfigure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_level', models.FloatField()),
                ('cpu_num', models.IntegerField()),
                ('flops', models.IntegerField()),
                ('mem_size', models.IntegerField()),
                ('IO_level', models.FloatField()),
                ('net_capacity', models.IntegerField()),
            ],
        ),
    ]
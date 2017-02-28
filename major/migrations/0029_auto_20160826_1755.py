# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-26 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0028_auto_20160826_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameterscore',
            name='cpu_all_cpi',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='parameterscore',
            name='cpu_all_idle',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='parameterscore',
            name='cpu_all_sywa',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='parameterscore',
            name='disk_all_read',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='parameterscore',
            name='disk_all_write',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='parameterscore',
            name='mem_all_mem_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='parameterscore',
            name='mem_all_swap_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='parameterscore',
            name='net_all_recv',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='parameterscore',
            name='net_all_send',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]

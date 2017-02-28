# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-26 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0029_auto_20160826_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speedconfigure',
            name='IO_level',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='speedconfigure',
            name='cpu_level',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='speedup',
            name='IO',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='speedup',
            name='compute',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='speedup',
            name='flops',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='speedup',
            name='mem',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='speedup',
            name='net',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]

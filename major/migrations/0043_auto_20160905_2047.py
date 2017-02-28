# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0042_jobabnormal_hostid'),
    ]

    operations = [
        migrations.AddField(
            model_name='benchmark',
            name='benchmark_total_consume_score',
            field=models.ForeignKey(related_name='benchmark_total_consume_score', default=1, to='major.ParameterScore'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parameterscore',
            name='nfs_all_in',
            field=models.DecimalField(default=1, max_digits=12, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parameterscore',
            name='nfs_all_out',
            field=models.DecimalField(default=1, max_digits=12, decimal_places=2),
            preserve_default=False,
        ),
    ]

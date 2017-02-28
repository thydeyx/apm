# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0012_auto_20160729_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='benchmark',
            name='benchmark_sorted_consume_score',
            field=models.ForeignKey(related_name='benchmark_sorted_consume_score', default=1, to='major.ParameterScore'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='benchmark',
            name='benchmark_time_density_score',
            field=models.ForeignKey(related_name='benchmark_time_density_score', default=1, to='major.ParameterScore'),
            preserve_default=False,
        ),
    ]

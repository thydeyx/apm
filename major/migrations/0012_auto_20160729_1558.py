# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0011_auto_20160729_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benchmark',
            name='sorted_consume_score',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='benchmark',
            name='time_density_score',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0013_auto_20160729_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='benchmark',
            name='sorted_consume_score',
        ),
        migrations.RemoveField(
            model_name='benchmark',
            name='time_density_score',
        ),
    ]

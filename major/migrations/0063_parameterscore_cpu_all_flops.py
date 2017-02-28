# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0062_auto_20161009_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameterscore',
            name='cpu_all_flops',
            field=models.DecimalField(default=1, max_digits=12, decimal_places=2),
            preserve_default=False,
        ),
    ]

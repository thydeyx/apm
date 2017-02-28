# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0063_parameterscore_cpu_all_flops'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobinfo',
            name='p_tag',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobinfo',
            name='phase_names',
            field=models.CharField(default=1, max_length=2048),
            preserve_default=False,
        ),
    ]

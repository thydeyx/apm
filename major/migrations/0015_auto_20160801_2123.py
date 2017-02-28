# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0014_auto_20160729_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobinfo',
            name='abnormal',
            field=models.ManyToManyField(to='major.JobAbnormal'),
        ),
        migrations.AddField(
            model_name='tasks',
            name='app_type',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

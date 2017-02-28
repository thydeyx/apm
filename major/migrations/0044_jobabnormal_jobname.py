# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0043_auto_20160905_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobabnormal',
            name='jobname',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0017_auto_20160801_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobinfo',
            name='job_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]

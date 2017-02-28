# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0015_auto_20160801_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='JobInfo',
            field=models.ManyToManyField(to='major.JobInfo'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='parameterconfigs',
            field=models.ManyToManyField(to='major.Parameters'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0016_auto_20160801_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nodeapp',
            name='app',
        ),
        migrations.RemoveField(
            model_name='nodeapp',
            name='node',
        ),
        migrations.RemoveField(
            model_name='nodejob',
            name='job',
        ),
        migrations.RemoveField(
            model_name='nodejob',
            name='node',
        ),
        migrations.RemoveField(
            model_name='parameterconfigs',
            name='parameter',
        ),
        migrations.DeleteModel(
            name='Applications',
        ),
        migrations.DeleteModel(
            name='NodeAPP',
        ),
        migrations.DeleteModel(
            name='NodeJob',
        ),
        migrations.DeleteModel(
            name='ParameterConfigs',
        ),
    ]

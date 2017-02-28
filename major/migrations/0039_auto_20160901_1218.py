# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0038_auto_20160901_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='info',
            field=models.CharField(max_length=255),
        ),
    ]

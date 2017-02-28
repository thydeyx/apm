# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0036_auto_20160901_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0030_auto_20160826_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='memory',
            field=models.FloatField(),
        ),
    ]

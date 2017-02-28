# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0066_auto_20161021_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='audit',
            field=models.CharField(default=b'unaudit', max_length=30),
        ),
    ]

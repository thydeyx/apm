# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0034_logs'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 1, 3, 31, 10, 381000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

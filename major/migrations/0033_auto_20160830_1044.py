# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0032_auto_20160830_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpu',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='net',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

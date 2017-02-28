# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0041_cmpconfigt'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobabnormal',
            name='hostid',
            field=models.CharField(default=111, max_length=60),
            preserve_default=False,
        ),
    ]

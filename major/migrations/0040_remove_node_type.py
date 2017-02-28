# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0039_auto_20160901_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='type',
        ),
    ]

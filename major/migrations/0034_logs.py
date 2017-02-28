# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0033_auto_20160830_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(max_length=255)),
                ('module', models.CharField(max_length=255)),
                ('info', models.TextField(max_length=255)),
                ('task', models.ForeignKey(to='major.Tasks')),
            ],
        ),
    ]

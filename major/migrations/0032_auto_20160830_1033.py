# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0031_auto_20160830_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('size', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Gpu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Net',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='node',
            name='cpu_frequency',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='node',
            name='memory_Speed',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='node',
            name='disk',
            field=models.ManyToManyField(to='major.Disk'),
        ),
        migrations.AddField(
            model_name='node',
            name='gpu',
            field=models.ManyToManyField(to='major.Gpu'),
        ),
        migrations.AddField(
            model_name='node',
            name='net',
            field=models.ManyToManyField(to='major.Net'),
        ),
    ]

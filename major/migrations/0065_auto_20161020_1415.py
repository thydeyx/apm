# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0064_auto_20161019_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhaseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nullType', models.IntegerField()),
                ('nullTypeName', models.CharField(max_length=1024)),
                ('cpuType', models.IntegerField()),
                ('cpuTypeName', models.CharField(max_length=1024)),
                ('networkType', models.IntegerField()),
                ('networkTypeName', models.CharField(max_length=1024)),
                ('diskType', models.IntegerField()),
                ('diskTypeName', models.CharField(max_length=1024)),
                ('memoryType', models.IntegerField()),
                ('memoryTypeName', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='RegressionAbnormal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('abnormal_num', models.IntegerField()),
                ('phase_names', models.CharField(max_length=1024)),
                ('abnormal_type', models.ForeignKey(to='major.AbnormalType')),
            ],
        ),
        migrations.RemoveField(
            model_name='speedtrend',
            name='configure',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='SpeedConfigure',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='SpeedTrend',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='SpeedUp',
        ),
        migrations.DeleteModel(
            name='SpeedConfigure',
        ),
        migrations.DeleteModel(
            name='SpeedTrend',
        ),
        migrations.DeleteModel(
            name='SpeedUp',
        ),
        migrations.AddField(
            model_name='tasks',
            name='regression_abnormalType',
            field=models.ManyToManyField(to='major.RegressionAbnormal', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='regression_reportType',
            field=models.ForeignKey(blank=True, to='major.PhaseType', null=True),
        ),
    ]

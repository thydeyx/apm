# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0018_jobinfo_job_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=512)),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='jobinfo',
            name='Suggestion',
            field=models.ManyToManyField(to='major.Suggestion'),
        ),
        migrations.AddField(
            model_name='tasks',
            name='Suggestion',
            field=models.ManyToManyField(to='major.Suggestion'),
        ),
    ]

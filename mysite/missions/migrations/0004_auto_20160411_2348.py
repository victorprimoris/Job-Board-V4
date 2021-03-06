# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 23:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0003_mission_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 11, 23, 48, 58, 130280, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='missions.Priority'),
        ),
    ]

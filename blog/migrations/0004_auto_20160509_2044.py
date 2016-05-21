# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-09 15:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160506_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('user', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2016, 5, 9, 15, 14, 52, 710000, tzinfo=utc))),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article'),
        ),
    ]

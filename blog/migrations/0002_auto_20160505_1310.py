# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-05 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
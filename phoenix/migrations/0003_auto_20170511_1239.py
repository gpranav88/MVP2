# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoenix', '0002_auto_20170511_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trigger',
            name='rules',
            field=models.CharField(max_length=50),
        ),
    ]

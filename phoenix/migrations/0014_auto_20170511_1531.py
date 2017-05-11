# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoenix', '0013_trigger_operation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trigger',
            name='operation',
            field=models.CharField(choices=[('lt', 'Less Than'), ('lte', 'Less Than Equal To'), ('eq', 'Equal To'), ('gte', 'Greater Than'), ('gt', 'Greater Than Equal TO')], default='lt', max_length=10),
        ),
    ]
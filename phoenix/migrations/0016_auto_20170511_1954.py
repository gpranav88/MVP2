# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 14:24
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('phoenix', '0015_auto_20170511_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='attributes',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('email', 'User Email'), ('cancelled_order', 'Cancelled Orders'), ('refund_order', 'Refund Orders')], default='email', max_length=10),
        ),
    ]

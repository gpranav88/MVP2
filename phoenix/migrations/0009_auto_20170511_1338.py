# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 08:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phoenix', '0008_auto_20170511_1337'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdminAction',
            new_name='Action',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 08:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phoenix', '0006_auto_20170511_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=50)),
                ('key', models.CharField(default='None', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='trigger',
            name='action_taken',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phoenix.Action'),
        ),
    ]

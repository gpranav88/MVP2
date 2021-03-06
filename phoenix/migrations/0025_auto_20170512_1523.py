# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 09:53
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('phoenix', '0024_auto_20170512_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trigger',
            name='action_taken',
        ),
        migrations.RemoveField(
            model_name='trigger',
            name='operation',
        ),
        migrations.AlterField(
            model_name='signal',
            name='attributes',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('email', 'User Email'), ('email_similarity', 'User Email Similarity'), ('cancelled_order', 'Cancelled Orders'), ('refund_order', 'Refund Orders'), ('order_count', 'Total Orders'), ('low_margin', 'Low Margin'), ('high_margin', 'High Margin'), ('amount', 'Amount'), ('amount_paid', 'Amount Paid')], default='email', max_length=105),
        ),
    ]

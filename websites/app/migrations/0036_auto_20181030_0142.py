# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-30 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_auto_20181028_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfomations',
            name='status_order',
            field=models.CharField(choices=[('cancel', 'Cancel'), ('waiting', 'Waiting'), ('accept', 'Accept'), ('shipping', 'Shipping'), ('done', 'Done')], default='create', max_length=255),
        ),
    ]

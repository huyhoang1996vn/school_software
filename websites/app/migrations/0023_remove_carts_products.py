# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-09 14:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20181008_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carts',
            name='products',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 20:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0006_auto_20170307_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='group',
        ),
    ]

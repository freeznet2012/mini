# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrc', '0009_rrc_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rrc',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]

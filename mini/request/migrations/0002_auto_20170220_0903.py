# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='contact',
            field=models.CharField(max_length=25),
        ),
    ]

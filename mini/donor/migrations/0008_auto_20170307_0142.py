# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0007_remove_donor_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
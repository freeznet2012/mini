# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0005_auto_20170307_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]

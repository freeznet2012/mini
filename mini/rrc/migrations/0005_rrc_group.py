# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('rrc', '0004_remove_rrc_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='rrc',
            name='group',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]
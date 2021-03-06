# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rrc', '0001_initial'),
        ('address', '0002_auto_20170213_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('contact', models.CharField(max_length=25)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.District')),
                ('rrc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrc.Rrc')),
            ],
        ),
    ]

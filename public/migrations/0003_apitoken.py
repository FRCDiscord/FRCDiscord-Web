# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 23:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_auto_20171028_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIToken',
            fields=[
                ('token', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
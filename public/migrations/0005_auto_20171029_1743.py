# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 17:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0004_apitoken_uses'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Member',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 19:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0007_auto_20171029_1930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='user_verified',
            new_name='verified_user',
        ),
    ]

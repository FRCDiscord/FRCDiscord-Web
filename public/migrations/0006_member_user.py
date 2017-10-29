# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 19:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('public', '0005_auto_20171029_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0010_mail_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='appeal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='public.Log'),
        ),
    ]

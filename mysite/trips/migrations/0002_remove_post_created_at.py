# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-11 09:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
    ]

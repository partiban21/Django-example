# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 03:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='pm',
        ),
    ]

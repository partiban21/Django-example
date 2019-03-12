# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('header', models.CharField(max_length=4096, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=4096)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
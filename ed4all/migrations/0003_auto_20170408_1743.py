# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-08 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ed4all', '0002_auto_20170408_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Student_ID',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]
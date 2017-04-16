# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-08 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ed4all', '0003_auto_20170408_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='id',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='Email_Address',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='id',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='id',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='id',
        ),
        migrations.RemoveField(
            model_name='request',
            name='id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Email_Address',
        ),
        migrations.RemoveField(
            model_name='student_advisor_counselor',
            name='Email_Address',
        ),
        migrations.RemoveField(
            model_name='student_advisor_counselor',
            name='id',
        ),
        migrations.AddField(
            model_name='faculty',
            name='F_Email',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='faculty',
            name='Faculty_ID',
            field=models.CharField(default='', max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='issue',
            name='Issue_ID',
            field=models.CharField(default='', max_length=4, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='request',
            name='Request_ID',
            field=models.CharField(default='', max_length=4, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='student',
            name='S_Email',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='student_advisor_counselor',
            name='C_Email',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='student_advisor_counselor',
            name='Counselor_ID',
            field=models.CharField(default='', max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='Course_ID',
            field=models.CharField(default='', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='Position',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='incident',
            name='Group_or_Individual',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='incident',
            name='Incident_ID',
            field=models.CharField(default='', max_length=4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='issue',
            name='Issue_Type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='Student_ID',
            field=models.CharField(default='', max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='GPA',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]

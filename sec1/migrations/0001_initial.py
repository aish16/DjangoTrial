# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dept_name', models.CharField(max_length=100)),
                ('Dept_head', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_name', models.CharField(max_length=250)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sec1.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.CharField(max_length=50)),
                ('end_date', models.CharField(max_length=50)),
                ('project_name', models.CharField(max_length=250)),
                ('supervisor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sec1.Employee')),
            ],
        ),
    ]

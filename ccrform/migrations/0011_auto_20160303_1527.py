# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-03 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccrform', '0010_auto_20160225_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccr',
            name='device_app',
            field=models.CharField(blank=True, choices=[('Device', 'Device'), ('Application', 'Application')], max_length=15, verbose_name='Device or Application'),
        ),
        migrations.AlterField(
            model_name='ccr',
            name='risk',
            field=models.CharField(choices=[('Low', 'Low'), ('Moderate', 'Moderate'), ('High', 'High')], max_length=8, null=True),
        ),
    ]

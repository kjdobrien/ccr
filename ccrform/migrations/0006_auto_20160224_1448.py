# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-24 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccrform', '0005_auto_20160224_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccr',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('For Review', 'For Review'), ('For Approval', 'For Approval'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Rejected for Amendments', 'Rejected for Amendments'), ('Complete', 'Complete')], default='Open', max_length=23),
        ),
    ]
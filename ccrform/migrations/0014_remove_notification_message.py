# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-10 12:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccrform', '0013_auto_20160310_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='message',
        ),
    ]
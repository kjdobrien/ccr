# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-24 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccrform', '0004_auto_20160223_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccr',
            name='comments_a',
            field=models.TextField(null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='ccr',
            name='comments_r',
            field=models.TextField(null=True, verbose_name='Comments'),
        ),
    ]
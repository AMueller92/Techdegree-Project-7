# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-03-21 15:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20190321_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='editor',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-21 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0009_remove_profile_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='comments',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='images.Comments'),
        ),
    ]

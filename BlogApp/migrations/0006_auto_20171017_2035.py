# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0005_auto_20171017_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='picture',
            field=models.ImageField(upload_to='img/blogs'),
        ),
        migrations.AlterField(
            model_name='learn',
            name='picture',
            field=models.ImageField(upload_to='img/learns'),
        ),
    ]

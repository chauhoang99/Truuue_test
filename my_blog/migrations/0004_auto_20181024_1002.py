# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 02:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_blog.Article'),
        ),
    ]
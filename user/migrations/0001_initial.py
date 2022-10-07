# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-09-24 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='姓名')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号码')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
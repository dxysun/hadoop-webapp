# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-21 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spark', '0002_fraudphone'),
    ]

    operations = [
        migrations.CreateModel(
            name='spiderphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.CharField(max_length=50)),
                ('mark', models.CharField(max_length=100)),
            ],
        ),
    ]

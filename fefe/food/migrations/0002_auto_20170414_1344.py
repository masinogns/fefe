# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-14 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BSSH_NM', models.CharField(blank=True, max_length=50, null=True)),
                ('TELNO', models.CharField(blank=True, max_length=20, null=True)),
                ('ADDR', models.CharField(blank=True, max_length=100, null=True)),
                ('MAIN_MENU', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Food',
        ),
    ]

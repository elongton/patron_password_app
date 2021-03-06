# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patron_password_app', '0003_auto_20170320_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googleaccount',
            name='password',
            field=models.CharField(blank=True, max_length=264),
        ),
        migrations.AlterField(
            model_name='googleaccount',
            name='username',
            field=models.CharField(blank=True, max_length=264),
        ),
        migrations.AlterField(
            model_name='hotmailaccount',
            name='password',
            field=models.CharField(blank=True, max_length=264),
        ),
        migrations.AlterField(
            model_name='hotmailaccount',
            name='username',
            field=models.CharField(blank=True, max_length=264),
        ),
        migrations.AlterField(
            model_name='otheraccount',
            name='password',
            field=models.CharField(blank=True, max_length=264),
        ),
        migrations.AlterField(
            model_name='otheraccount',
            name='service',
            field=models.CharField(blank=True, max_length=264),
        ),
        migrations.AlterField(
            model_name='otheraccount',
            name='username',
            field=models.CharField(blank=True, max_length=264),
        ),
        migrations.AlterField(
            model_name='patron',
            name='phone_number',
            field=models.CharField(blank=True, max_length=24),
        ),
        migrations.AlterField(
            model_name='yahooaccount',
            name='password',
            field=models.CharField(blank=True, max_length=264),
        ),
        migrations.AlterField(
            model_name='yahooaccount',
            name='username',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]

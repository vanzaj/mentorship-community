# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-31 09:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='name',
            field=models.CharField(help_text='Module Name', max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='name',
            field=models.CharField(help_text='Track Name', max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='modules', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(help_text='Skill Name', max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='prerequisites',
            field=models.ManyToManyField(blank=True, to='skills.Skill'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='skills', to=settings.AUTH_USER_MODEL),
        ),
    ]

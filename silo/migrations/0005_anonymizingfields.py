# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-05 21:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('silo', '0004_mergedsilosfieldmapping_merge_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymizingFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldname', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateTimeField(editable=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

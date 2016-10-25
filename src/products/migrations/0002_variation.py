# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('car_year', models.CharField(max_length=120)),
                ('car_manufacturer', models.CharField(max_length=120)),
                ('car_type', models.CharField(max_length=120)),
                ('car_model', models.CharField(max_length=120)),
                ('description', models.TextField(null=True, blank=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]

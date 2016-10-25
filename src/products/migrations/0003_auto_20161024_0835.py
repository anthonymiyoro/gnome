# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='description',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='variation',
            old_name='active',
            new_name='new',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='car_manufacturer',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='car_model',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='car_type',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='car_year',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='title',
        ),
    ]

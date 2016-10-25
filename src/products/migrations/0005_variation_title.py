# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_variation_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='title',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]

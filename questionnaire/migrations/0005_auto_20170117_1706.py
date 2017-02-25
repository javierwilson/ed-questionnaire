# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0004_auto_20161219_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='value',
            field=models.CharField(max_length=120, verbose_name='Short Value'),
            preserve_default=True,
        ),
    ]

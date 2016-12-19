# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0003_auto_20161219_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='score',
            field=models.DecimalField(null=True, verbose_name='Score', max_digits=5, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choice',
            name='text_es',
            field=models.CharField(default='', max_length=200, verbose_name='Choice Text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='extra_es',
            field=models.CharField(help_text='Extra information (use  on question type)', max_length=512, null=True, verbose_name='Extra information', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='footer_es',
            field=models.TextField(help_text=b'Footer rendered below the question interpreted as textile', verbose_name='Footer', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='text_es',
            field=models.TextField(verbose_name='Text', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='questionset',
            name='text_es',
            field=models.TextField(default='', help_text=b"This is interpreted as Textile: <a href='http://en.wikipedia.org/wiki/Textile_%28markup_language%29' target='_blank'>http://en.wikipedia.org/wiki/Textile_(markup_language)</a>", verbose_name='Text'),
            preserve_default=False,
        ),
    ]

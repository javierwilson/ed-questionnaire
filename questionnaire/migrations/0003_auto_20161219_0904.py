# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_question_sort_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='score',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        #migrations.AddField(
        #    model_name='choice',
        #    name='score',
        #    field=models.DecimalField(null=True, verbose_name='Score', max_digits=5, decimal_places=2, blank=True),
        #    preserve_default=True,
        #),
        #migrations.AddField(
        #    model_name='choice',
        #    name='text_es',
        #    field=models.CharField(default='', max_length=200, verbose_name='Choice Text'),
        #    preserve_default=False,
        #),
        #migrations.AddField(
        #    model_name='question',
        #    name='extra_es',
        #    field=models.CharField(help_text='Extra information (use  on question type)', max_length=512, null=True, verbose_name='Extra information', blank=True),
        #    preserve_default=True,
        #),
        #migrations.AddField(
        #    model_name='question',
        #    name='footer_es',
        #    field=models.TextField(help_text=b'Footer rendered below the question interpreted as textile', verbose_name='Footer', blank=True),
        #    preserve_default=True,
        #),
        #migrations.AddField(
        #    model_name='question',
        #    name='text_es',
        #    field=models.TextField(verbose_name='Text', blank=True),
        #    preserve_default=True,
        #),
        #migrations.AddField(
        #    model_name='questionset',
        #    name='text_es',
        #    field=models.TextField(default='', help_text=b"This is interpreted as Textile: <a href='http://en.wikipedia.org/wiki/Textile_%28markup_language%29' target='_blank'>http://en.wikipedia.org/wiki/Textile_(markup_language)</a>", verbose_name='Text'),
        #    preserve_default=False,
        #),
        migrations.AlterField(
            model_name='choice',
            name='text_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Choice Text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='footer_en',
            field=models.TextField(help_text=b'Footer rendered below the question interpreted as textile', null=True, verbose_name='Footer', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='redirect_url',
            field=models.CharField(default=b'/static/complete.html', max_length=128, null=True, help_text=b'URL to redirect to when Questionnaire is complete. Macros: $SUBJECTID, $RUNID, $LANG', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questionset',
            name='text_en',
            field=models.TextField(help_text=b"This is interpreted as Textile: <a href='http://en.wikipedia.org/wiki/Textile_%28markup_language%29' target='_blank'>http://en.wikipedia.org/wiki/Textile_(markup_language)</a>", null=True, verbose_name='Text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='language',
            field=models.CharField(default=b'es', max_length=2, verbose_name='Language', choices=[(b'es', 'Espa\xf1ol'), (b'en', 'English')]),
            preserve_default=True,
        ),
    ]

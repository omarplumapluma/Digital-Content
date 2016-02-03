# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_content', '0009_campaing_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaing_media',
            name='campaing',
            field=models.ForeignKey(default=0, verbose_name='Campa\xf1a', to='company_content.Company_content'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campaing_media',
            name='status',
            field=models.CharField(default='a', max_length=1, choices=[(b'a', b'Activo'), (b'i', b'Inactivo')]),
            preserve_default=False,
        ),
    ]

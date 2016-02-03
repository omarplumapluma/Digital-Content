# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_content', '0010_auto_20160126_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaing_media',
            name='content',
            field=models.CharField(max_length=100, verbose_name='Contenido'),
        ),
    ]

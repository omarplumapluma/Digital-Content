# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_content', '0002_company_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company_media',
            name='File',
        ),
        migrations.AddField(
            model_name='company_media',
            name='files',
            field=models.FileField(default=0, upload_to=b'/static/media'),
            preserve_default=False,
        ),
    ]

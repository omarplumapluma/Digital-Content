# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_content', '0004_auto_20160121_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_media',
            name='files',
            field=models.FileField(upload_to=b'content'),
        ),
    ]
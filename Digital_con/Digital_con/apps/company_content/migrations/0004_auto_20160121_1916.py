# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_content', '0003_auto_20160121_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_media',
            name='files',
            field=models.FileField(upload_to=b'Digital_con'),
        ),
    ]

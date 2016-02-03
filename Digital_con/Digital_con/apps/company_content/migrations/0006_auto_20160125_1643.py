# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company_content', '0005_auto_20160122_0116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company_media',
            options={'ordering': ['create_date']},
        ),
        migrations.AddField(
            model_name='company_media',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 25, 16, 43, 36, 667711, tzinfo=utc), verbose_name=b'Fecha de ceaci\xc3\xb3n', auto_now_add=True),
            preserve_default=False,
        ),
    ]

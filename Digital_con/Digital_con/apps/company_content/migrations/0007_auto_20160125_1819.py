# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Digital_con.apps.company_content.models


class Migration(migrations.Migration):

    dependencies = [
        ('company_content', '0006_auto_20160125_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_media',
            name='files',
            field=models.FileField(upload_to=Digital_con.apps.company_content.models._get_upload_to),
        ),
    ]

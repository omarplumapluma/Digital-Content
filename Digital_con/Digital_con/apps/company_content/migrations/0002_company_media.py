# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('company_content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('File', models.FileField(upload_to=b'/Digital_con/media')),
                ('company', models.ForeignKey(verbose_name='Compa\xf1ia', to='company.Company')),
            ],
        ),
    ]

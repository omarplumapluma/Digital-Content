# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20160125_1659'),
        ('company_content', '0008_auto_20160125_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaing_media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de ceaci\xc3\xb3n')),
                ('company', models.ForeignKey(verbose_name='Compa\xf1ia', to='company.Company')),
                ('content', models.ForeignKey(verbose_name='Contenido', to='company_content.Company_media')),
            ],
            options={
                'ordering': ['create_date'],
            },
        ),
    ]

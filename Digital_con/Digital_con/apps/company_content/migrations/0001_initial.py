# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campaign', models.CharField(max_length=100, verbose_name='Campa\xf1a')),
                ('description', models.CharField(max_length=100, verbose_name='Descripci\xf3n')),
                ('start_date', models.DateTimeField(verbose_name=b'Fecha inicio')),
                ('end_date', models.DateTimeField(verbose_name=b'Fecha fin')),
                ('marquee', models.TextField(verbose_name=b'Marquee')),
                ('status', models.CharField(max_length=1, choices=[(b'a', b'Activo'), (b'i', b'Inactivo')])),
                ('company', models.ForeignKey(verbose_name='Compa\xf1ia', to='company.Company')),
            ],
            options={
                'ordering': ['campaign'],
                'verbose_name': 'content',
                'verbose_name_plural': 'contents',
            },
        ),
    ]

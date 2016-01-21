# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=1, choices=[(b'a', b'Activo'), (b'i', b'Inactivo')])),
                ('name', models.CharField(max_length=120, verbose_name=b'Nombre')),
                ('rfc', models.CharField(max_length=15, verbose_name=b'RFC')),
                ('street', models.CharField(max_length=60, verbose_name=b'Calle')),
                ('colony', models.CharField(max_length=60, verbose_name=b'Colonia')),
                ('city', models.CharField(max_length=30, verbose_name=b'Ciudad')),
                ('state', models.CharField(max_length=30, verbose_name=b'Estado')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'comapny',
                'verbose_name_plural': 'comapnies',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_contact', models.CharField(max_length=30, verbose_name=b'Contacto')),
                ('phone_contact', models.CharField(max_length=15, verbose_name=b'Telefono')),
                ('movil', models.CharField(max_length=15, verbose_name=b'Celular')),
                ('email', models.EmailField(max_length=60, verbose_name=b'Email')),
                ('company', models.ForeignKey(related_name='company', to='company.Company')),
            ],
            options={
                'ordering': ['name_contact'],
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
        ),
    ]

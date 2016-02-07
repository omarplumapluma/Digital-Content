# -*- coding: utf-8 -*-
import os
import uuid

from django.db import models
from django.dispatch import receiver
from Digital_con.apps.company.models import Company

# Create your models here.
class Company_content(models.Model):

    """A model."""
    STATUS = (
        ('a', "Activo"),
        ('i', "Inactivo"),
    )

    company = models.ForeignKey(Company, verbose_name=u"Compañia")
    campaign = models.CharField(max_length=100, verbose_name=u"Campaña")
    description = models.CharField(max_length=100, verbose_name=u"Descripción")
    start_date = models.DateTimeField(verbose_name="Fecha inicio")
    end_date = models.DateTimeField(verbose_name="Fecha fin")
    marquee = models.TextField(verbose_name="Marquee")
    status = models.CharField(max_length=1, choices=STATUS)

    class Meta:
        ordering = ['campaign']
        verbose_name = 'content'
        verbose_name_plural = 'contents'

    def __str__(self):
        return self.campaign

    def get_content_detail_url(self):
        return u"/company_content/detail/%i" % self.id


def _get_upload_to(instance, filename):
    return ''.join([filename])


class Company_media(models.Model):

    company = models.ForeignKey(Company, verbose_name=u"Compañia")
    files = models.FileField(upload_to="content")
    create_date = models.DateTimeField(verbose_name="Fecha de ceación", auto_now_add=True)

    class Meta:
        ordering = ['create_date']

    def __str__(self):
        return self.company

    def __unicode__(self):
        return unicode(self.files)


@receiver(models.signals.post_delete, sender=Company_media)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `Company_media` object is deleted.
    """
    if instance.files:
        if os.path.isfile(instance.files.path):
            os.remove(instance.files.path)

class Campaing_media(models.Model):

    """A model."""
    STATUS = (
        ('a', "Activo"),
        ('i', "Inactivo"),
    )

    company = models.ForeignKey(Company, verbose_name=u"Compañia")
    campaing = models.ForeignKey(Company_content, verbose_name=u"Campaña")
    content = models.CharField(max_length=100, verbose_name=u"Contenido")
    create_date = models.DateTimeField(verbose_name="Fecha de ceación", auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS)

    class Meta:
        ordering = ['create_date']
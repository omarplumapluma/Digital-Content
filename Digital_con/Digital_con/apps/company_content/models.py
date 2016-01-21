# -*- coding: utf-8 -*-
from django.db import models
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
        return self.company

    def get_content_detail_url(self):
        return u"/company_content/detail/%i" % self.id


class Company_media(models.Model):

    company = models.ForeignKey(Company, verbose_name=u"Compañia")
    files = models.FileField(upload_to='Digital_con')

    def __str__(self):
        return self.company

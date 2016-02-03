from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):

    """A model."""
    status = models.CharField(choices=(
        ('a', "Activo"),
        ('i', "Inactivo"),
    ), max_length=1)
    name = models.CharField(verbose_name="Nombre", max_length=120, null=False)
    rfc = models.CharField(verbose_name="RFC", max_length=15, null=False)
    street = models.CharField(verbose_name="Calle", max_length=60, null=False)
    colony = models.CharField(verbose_name="Colonia", max_length=60, null=False)
    city = models.CharField(verbose_name="Ciudad", max_length=30, null=False)
    state = models.CharField(verbose_name="Estado", max_length=30, null=False)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['name']
        verbose_name = 'comapny'
        verbose_name_plural = 'comapnies'

    def __str__(self):
        return self.name

    # count contacto by empresa
    def get_contacts_count(self):
        return self.company.count()

    def get_company_detail_url(self):
        return u"/company/detail/%i" % self.id


class Contact(models.Model):

    """contact"""
    name_contact = models.CharField(verbose_name="Contacto", max_length=30, null=False)
    phone_contact = models.CharField(verbose_name="Telefono", max_length=15, null=False)
    movil = models.CharField(verbose_name="Celular", max_length=15, null=False)
    email = models.EmailField(verbose_name="Email", max_length=60, null=False)

    company = models.ForeignKey("Company", related_name='company')

    class Meta:
        ordering = ['name_contact']
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.name_contact

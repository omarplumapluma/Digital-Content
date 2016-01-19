from django.forms import ModelForm
from .models import Company, Contact

class CompanyForm(ModelForm):

    class Meta:
        model = Company


class ContactForm(ModelForm):

    class Meta:
        model = Contact
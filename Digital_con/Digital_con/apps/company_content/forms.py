from django.forms import ModelForm
from .models import Company_content
from django.contrib.auth.models import User
from datetimewidget.widgets import DateTimeWidget

class CompanyContentForm(ModelForm):

    class Meta:
        model = Company_content


user = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')

class yourForm(forms.ModelForm):
    class Meta:
        model = yourModel
        widgets = {
            #Use localization and bootstrap 3
            'datetime': DateTimeWidget(attrs={'id':"yourdatetimeid"}, usel10n = True, bootstrap_version=3)
        }
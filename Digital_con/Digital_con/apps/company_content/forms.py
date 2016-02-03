from django.forms import ModelForm
from .models import Campaing_media, Company_content
from datetimewidget.widgets import DateTimeWidget

class CampaingForm(ModelForm):

    class Meta:
        model = Campaing_media
        fields = ['company', 'content', 'campaing', 'status']

class CompanyContentForm(ModelForm):

    class Meta:
        model = Company_content
        fields = ['company', 'campaign', 'description', 'start_date', 'end_date', 'marquee', 'status']
        
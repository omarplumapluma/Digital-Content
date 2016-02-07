from django.forms import ModelForm
from .models import Campaing_media, Company_content
from bootstrap3_datetime.widgets import DateTimePicker

class CampaingForm(ModelForm):

    class Meta:
        model = Campaing_media
        fields = ['company', 'content', 'campaing', 'status']

class CompanyContentForm(ModelForm):

    class Meta:
        model = Company_content
        fields = ['company', 'campaign', 'description', 'start_date', 'end_date', 'marquee', 'status']
        widgets = {
            #Use localization and bootstrap 3
            'start_date': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                                       "pickSeconds": False}),
            'end_date': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                                       "pickSeconds": False})
           
        }

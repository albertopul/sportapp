from django.forms import ModelForm
from django import forms
from .models import Athlete


class AthleteForm(ModelForm):
    class Meta:
        model = Athlete
        fields = ['name', 'featured_image', 'description', 'highlight_image', 
                'social_facebook', 'social_youtube', 'social_website', 'social_mail']

    def __init__(self, *args, **kwargs):
        super(AthleteForm, self).__init__(*args, **kwargs)


        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
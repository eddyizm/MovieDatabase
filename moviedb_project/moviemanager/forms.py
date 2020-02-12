from django import forms
from django.db import models
from datetime import datetime
from .models import *
import datetime

current_year = datetime.date.today().year

class NameForm(forms.Form):
    movie_title = forms.CharField(label = 'Movie Name',max_length = 100)
    dvd_name = forms.CharField(label = 'DVD',max_length = 100, required = False)
    form_field = forms.CharField(label = 'Form',max_length = 100, required = False)
    genre_field = forms.CharField(label = 'Genre',max_length = 100, required = False)
    year_field = forms.IntegerField(min_value = 1900, max_value = current_year)
    alt_title_field1 = forms.CharField(label = 'Alt Title 1',max_length = 100, required = False)
    alt_title_field2 = forms.CharField(label = 'Alt Title 2',max_length = 100, required = False)
    count_field = forms.CharField(label = 'Alt Title 2',max_length = 100, required = False)
    director_field = forms.DateField(label = 'Director', required = False)
    language_field = forms.DateField(label = 'Language', required = False)
    date_watched_field = forms.DateField(label = 'Date Watched', required = False)
    spec_field = forms.DateField(label = 'Spec', required = False)
    def clean_movie_name(self):
        title_data = self.cleaned_data['movie_name']
        #print(title_data)
        return title_data
    #post = forms.CharField

'''class Year(models.Model):
    year_field = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)'''
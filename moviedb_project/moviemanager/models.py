from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

#current_year = datetime.date.today().year
'''def current_year():
    return datetime.date.today().year'''
def max_year():
    year = datetime.date.today().year
    return year

database_filters = ( 
    ('movie_title', 'Movie Title'),
    ('dvd_name', 'DVD Name'),
    ('form_field', 'Form Field'),
    ('genre', 'Genre'),
    ('year', 'Year'),
    ('alt_title_1', 'Alt Title 1'),
    ('alt_title_2', 'Alt Title 2'),
    ('count', 'Count'),
    ('director', 'Director'),
    ('language', 'Language'),
    ('date_watched', 'Date Watched'),
    ('spec', 'Spec')
)


#class NameFormModel(models.Model):
class MovieEntry(models.Model):        
    min_year = 1900
    #max_year = datetime.datetime.year
    movie_title = models.CharField(max_length = 100)
    dvd_name = models.CharField(max_length = 100, blank = True)
    form_field = models.CharField(max_length = 100, blank = True)
    genre = models.CharField(max_length = 100, blank = True)
    #year_field = models.DateField(auto_now=False, auto_now_add=False)
    year = models.IntegerField(blank = True, default = min_year, validators = [MinValueValidator(min_year), MaxValueValidator(max_year())])
    alt_title_1 = models.CharField(max_length = 100, blank = True)
    alt_title_2 = models.CharField(max_length = 100, blank = True)
    count  = models.CharField(max_length = 100, blank = True)
    director = models.CharField(max_length = 100, blank = True)
    language = models.CharField(max_length = 100, blank = True)
    date_watched = models.DateField(auto_now=False, auto_now_add=False)
    spec = models.CharField(max_length = 100, blank = True)

class SearchFormModel(models.Model):
    search_filter = models.CharField(max_length = 100, choices=database_filters, default = 'Filter')
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class NameFormModel(models.Model):
    movie_title = models.CharField(max_length = 100)
    dvd_name = models.CharField(max_length = 100)
    form_field = models.CharField(max_length = 100)
    genre_field = models.CharField(max_length = 100)
    year_field = models.IntegerField()
    alt_title_field1 = models.CharField(max_length = 100)
    alt_title_field2 = models.CharField(max_length = 100)
    count_field = models.CharField(max_length = 100)
    director_field = models.DateField()
    language_field = models.DateField()
    date_watched_field = models.DateField()
    spec_field = models.DateField()
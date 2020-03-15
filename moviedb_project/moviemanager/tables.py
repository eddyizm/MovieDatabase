'''
import django_tables2 as tables
from .models import MovieEntry

class MovieTable(tables.Table):
    #MovieTableExtraColumn = tables.Column(accessor = 'extra_column', verbose_name = 'extra_column')
    class Meta:
        model = MovieEntry'''
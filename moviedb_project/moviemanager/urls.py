from django.urls import path, re_path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('search/', views.search, name = 'search')
]

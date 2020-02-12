from django.urls import path, re_path
from . import views


urlpatterns = [
    path('moviemanagerView', views.moviemanagerView, name='moviemanagerView'),
    path('',views.moviemanager, name='moviemanager'),
    path('',views.about_page),
    path('',views.contact_page)
]
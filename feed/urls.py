from django.urls import path

from . import views

app_name = 'feed'
urlpatterns = [
    path('', views.index, name='index'),
    path('sources/add/', views.sources_add, name="sources_add")
]

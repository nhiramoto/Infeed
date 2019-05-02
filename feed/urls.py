from django.urls import path

from . import views

app_name = 'feed'
urlpatterns = [
    path('', views.index, name='index'),
    path('lists/add/', views.lists_add, name="lists_add"),
    path('sources/add/', views.sources_add, name="sources_add")
]

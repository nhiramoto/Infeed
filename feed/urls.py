from django.urls import path

from . import views

app_name = 'feed'
urlpatterns = [
    path('', views.login, name='login'),
    path('all/', views.all, name='all'),
    path('user/login', views.user_login, name="user_login"),
    path('lists/add/', views.lists_add, name="lists_add"),
    path('sources/add/', views.sources_add, name="sources_add")
]

"""
Infeed URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='feed/')),
    path('feed/', include('feed.urls')),
    path('admin/', admin.site.urls),
]

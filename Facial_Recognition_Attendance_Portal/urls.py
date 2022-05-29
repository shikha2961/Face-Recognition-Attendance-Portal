"""Facial_Recognition_Attendance_Portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Facial_Recognition_Attendance_Portal.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

# Customize the Django Administration
admin.site.site_header = "Admin Login"
admin.site.site_title = "Regsiter New Student"
admin.site.index_title = "Welcome to the Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Features.urls')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


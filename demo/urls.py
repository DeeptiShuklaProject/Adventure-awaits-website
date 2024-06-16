"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import django
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from demo import forms, views

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('',views.homePage,name='home'),
    path('about-us/',views.aboutUs,name='about'),
    path('contact/',views.contact,name='contact'),
    path('saveenquiry/',views.saveEnquiry,name='saveenquiry'),
    path('services/',views.services,name='services'),
    path('submitform/',views.submitform,name="submitform"),
    path('destinations/',views.destinations,name='destinations'),
    path('gallery/',views.gallery,name='gallery'),
    path('userform/',views.userform,name='userform'),
    path('calculator/',views.calculator,name='calculator'),
    path('saveevenodd/',views.saveevenodd,name='saveevenodd'),
    path('AdvanceCalculator/',views.AdvanceCalculator,name='AdvanceCalculator'),
    path('marksheet/',views.marksheet,name='marksheet'),
    path('newsdetails/<slug>',views.newsDetails),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

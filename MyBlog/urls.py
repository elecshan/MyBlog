"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from BlogApp import views
from DjangoUeditor import urls as UEditor_url

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^home', views.home),
    url(r'^blogPage', views.getBlogPage),
    url(r'^life', views.life),
    url(r'^learn', views.learn),
    url(r'^contact', views.contact),
    url(r'^processcontact', views.processcontact),
    url(r'^about', views.about),
    url(r'^ueditor/', include(UEditor_url)),
]

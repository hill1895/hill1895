# -*- coding: UTF-8 -*-
# coding=UTF-8

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap, index
from django.contrib.sitemaps import views
from hill1895.sitemap import sitemaps
from hill1895.models import Blog, Tag
from hill1895 import views
from hill1895.LatestEntriesFeed import LatestEntriesFeed

urlpatterns = patterns('hill1895.views',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^ueditor/', include('DjangoUeditor.urls')),
                       url(r'^favicon.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
                       url(r'^$', 'index', name='index'),
                       url(r'^blog_detail/blog_(?P<blog_id>\d+)/$', 'blog_detail', name='blog_detail'),
                       url(r'^tag_(?P<tag_id>\d+)/$', 'tag', name='tag'),
                       url(r'^geek/$', 'geek', name='geek'),
                       url(r'^essay/$', 'essay', name='essay'),
                       url(r'^joke/$', 'joke', name='joke'),
                       url(r'^profile/$', 'profile', name='profile'),
                       url(r'^robots\.txt$',
                           TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
                       url(r'^sitemap\.xml$', index, {'sitemaps': sitemaps}),
                       url(r'^sitemap-(?P<section>.+)\.xml$', sitemap, {'sitemaps': sitemaps}),
                       url(r'^feed/main\.xml$', LatestEntriesFeed()),
                       )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

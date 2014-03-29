#coding=utf-8
#!/usr/bin/python

from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)

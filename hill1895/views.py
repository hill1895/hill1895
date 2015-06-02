#-*- coding: UTF-8 -*-
#coding=UTF-8

from django.shortcuts import render_to_response
from django import template
from hill1895.models import Blog,Tag

# Create your views here.

def index(request):
	blogs=Blog.objects.order_by('-pub_time')
	tags=Tag.objects.order_by('-add_time')
	return render_to_response('index.html',{'blogs':blogs,'tags':tags})
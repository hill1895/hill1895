#-*- coding: UTF-8 -*-
#coding=UTF-8

from django.shortcuts import render_to_response
from django import template
from hill1895.models import Blog,Tag

# Create your views here.


def __get_latest(blogs):

	obj_num=blogs.count()
	latest=[]

	if obj_num>3:
		for i in range(3):
			latest.append([blogs[i].title,blogs[i].id]) 
	else:
		for i in range(obj_num):
			latest.append([blogs[i].title,blogs[i].id]) 

	return latest

def __get_blog_info(blogs):

	#exclude blog content!
	blog_info=[]

	for blog in blogs:
		blog_info.append({'title':blog.title,
			'id':blog.id,
			'head_pic_url':blog.head_pic_url,
			'pub_time':blog.pub_time,
			'page_views':blog.page_views})

	return blog_info




def index(request):
	blogs=Blog.objects.all().order_by('-pub_time')
	tags=Tag.objects.all().order_by('-add_time')
	latest=__get_latest(blogs)
	blog_infos=__get_blog_info(blogs)
	content={'blog_infos':blog_infos,
			 'tags':tags,
			 'latest':latest}
	return render_to_response('index.html',content)

def blog_detail(request,blog_id):
	blog=Blog.objects.get(id=blog_id)
	blog.page_views+=1
	blog.save()
	blog_tags=blog.tags.all()
	return render_to_response('detail.html',{'blog':blog,'blog_tags':blog_tags})
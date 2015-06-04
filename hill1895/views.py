#-*- coding: UTF-8 -*-
#coding=UTF-8

from django.shortcuts import render_to_response
from django import template
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from hill1895.models import Blog,Tag,Category1,Category2

# Create your views here.

#some function would be used in views
def __get_latest(objs,max_num=8):

	obj_num=objs.count()
	latest=[]

	if obj_num>max_num:
		for i in range(max_num):
			latest.append({'title':objs[i].title,'id':objs[i].id}) 
	else:
		for i in range(obj_num):
			latest.append({'title':objs[i].title,'id':objs[i].id})

	return latest

def __get_blog_info(objs):

	#exclude blog content!
	blog_info=[]

	for blog in objs:
		blog_info.append({'title':blog.title,
			'id':blog.id,
			'head_pic_url':blog.head_pic_url,
			'pub_time':blog.pub_time,
			'page_views':blog.page_views})

	return blog_info

def __my_pagination(request,objs,display_num=6,after_range=6,before_range=5):
	paginator=Paginator(objs,display_num)

	try:
		page=int(request.GET.get('page'))
	except:
		page=1
	try:
		objects=paginator.page(page)
	except EmptyPage:
		objects=paginator.page(paginator.num_pages)
	except:
		objects=paginator.page(1)

	if page>after_range:
		page_range=paginator.page_range[page-after_range:page+before_range]
	else:
		page_range=paginator.page_range[0:page+before_range]

	
	return objects,page_range

def __get_blog_list(request,obj_list):
	obj_latest=__get_latest(obj_list)
	obj_infos_all=__get_blog_info(obj_list)
	obj_infos,obj_page_range=__my_pagination(request,obj_infos_all)

	return obj_latest,obj_infos,obj_page_range


def __blog_by_category2(request,objs,category):
	obj_category=Category2.objects.get(category_2=category)
	obj_list=objs.filter(category2=obj_category)
	obj_infos_all=__get_blog_info(obj_list)
	obj_infos,obj_page_range=__my_pagination(request,obj_infos_all)

	return obj_infos,obj_page_range




###the views of the page


def index(request):
	blogs=Blog.objects.all()
	tags=Tag.objects.all()
	latest,blog_infos,page_range=__get_blog_list(request,blogs)
	content={'blog_infos':blog_infos,
			 'page_range':page_range,
			 'tags':tags,
			 'latest':latest}
	return render_to_response('index.html',content)

def blog_detail(request,blog_id):
	blog=Blog.objects.get(id=blog_id)
	blog.page_views+=1
	blog.save()
	blog_tags=blog.tags.all()
	return render_to_response('detail.html',{'blog':blog,'blog_tags':blog_tags})


def tag(request,tag_id):

	get_tag=Tag.objects.get(id=tag_id)
	blogs=Blog.objects.filter(tags=get_tag)
	tags=Tag.objects.all()
	tag_latest,tag_infos,page_range=__get_blog_list(request,blogs)

	content={'tag_infos':tag_infos,
			 'page_range':page_range,
			 'tag_latest':tag_latest,
			 'get_tag':get_tag,
			 'tags':tags}

	return render_to_response('tag.html',content)


def geek(request):

	geek=Category1.objects.get(category_1='geek')
	blogs_geek=Blog.objects.filter(category1=geek)

	tags=Tag.objects.all()
	
	geek_latest,geek_infos,geek_page_range=__get_blog_list(request,blogs_geek)
	
	cpp_infos,cpp_page_range=__blog_by_category2(request,blogs_geek,'c/c++')
	python_infos,python_page_range=__blog_by_category2(request,blogs_geek,'python/django')
	website_infos,website_page_range=__blog_by_category2(request,blogs_geek,'website')

	content={'geek_infos':geek_infos,
			 'geek_page_range':geek_page_range,
			 'cpp_infos':cpp_infos,
			 'cpp_page_range':cpp_page_range,
			 'python_infos':python_infos,
			 'python_page_range':python_page_range,
			 'website_infos':website_infos,
			 'website_page_range':website_page_range,
			 'geek_latest':geek_latest,
			 'tags':tags}

	return render_to_response('geek.html',content)


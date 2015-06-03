#coding:utf-8

from django import template

register=template.Library()

@register.filter(name='get_value')
#get list or dict value
def get_value(value,arg):
	return value[arg]



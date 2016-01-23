#-*- coding:utf8 -*-
from django.contrib.syndication.views import Feed
from hill1895.models import Blog

class LatestEntriesFeed(Feed):

    title = u"刘文图熙1895最新的文章"
    link = "hill1895.rocks"
    description = "关注刘文图熙1895的最新动态"

    def items(self):

        return Blog.objects.order_by('-pub_time')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return "hill1895.rocks/blog_detail/blog_"+str(item.id)
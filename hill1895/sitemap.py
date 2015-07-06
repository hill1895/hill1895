from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from hill1895.models import Blog,Tag,Category1,Category2,Profile,Profile_Tag,Friend,Friend_Tag

class IndexSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'daily'
    lastmod=Blog.objects.all()[0].pub_time

    def items(self):
    	return ['index']

    def location(self, item):
        return ''



class CategoryViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['geek', 'essay','joke']

    def lastmod(self,item):
    	category=Category1.objects.get(category_1=item)
    	return Blog.objects.filter(category1=category)[0].pub_time

    def location(self, item):
        return '/'+item

class ProfileViewSitemap(sitemaps.Sitemap):
    priority = 0.3
    changefreq = 'monthly'

    def items(self):
        return ['profile']

    def lastmod(self,item):
    	return Profile.objects.get(title='Updates').pub_time

    def location(self, item):
        return '/'+item

class BlogViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'yearly'

    def items(self):
        return Blog.objects.all()

    def lastmod(self,item):
    	return item.pub_time

    def location(self, item):
        return '/blog_detail/blog_'+str(item.id)

class TagViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return Tag.objects.all()

    def lastmod(self,item):
    	return item.add_time

    def location(self, item):
        return '/tag_'+str(item.id)

sitemaps = {
    'category':CategoryViewSitemap,
    'index':IndexSitemap,
    'profile':ProfileViewSitemap,
    'blogs':BlogViewSitemap,
    'tags':TagViewSitemap
}
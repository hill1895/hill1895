from django.db import models
from DjangoUeditor.models import UEditorField

class Category1(models.Model):
	category_1=models.CharField(max_length=30,db_index=True,unique=True)
	def __unicode__(self):
		return self.category_1

class Category2(models.Model):
	category_2=models.CharField(max_length=30,db_index=True,unique=True)
	def __unicode__(self):
		return self.category_2


class Tag(models.Model):
	tag=models.CharField(max_length=30,db_index=True,unique=True)
	def __unicode__(self):
		return self.tag
				

class Blog(models.Model):
	title=models.CharField(u'Title',max_length=100)
	head_pic_url=models.CharField(u'Head_pic_url',max_length=250,null=True,blank=True)
	pub_time=models.DateTimeField(auto_now=True)
	content=UEditorField(u'content',width=900,height=600,toolbars="full",imagePath="",settings={})
	page_views=models.PositiveIntegerField(u'page_views',default=0,editable=False)
	category1=models.ForeignKey(Category1)
	category2=models.ForeignKey(Category2,null=True)
	tags=models.ManyToManyField(Tag,blank=True)
	def __unicode__(self):
		return self.title




from django.db import models
from DjangoUeditor.models import UEditorField

class Category1(models.Model):
	category_1=models.CharField(max_length=30,db_index=True,unique=True)
	pub_time=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.category_1

	class Meta:
		ordering=['-pub_time']

class Category2(models.Model):
	category_2=models.CharField(max_length=30,db_index=True,unique=True)
	pub_time=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.category_2

	class Meta:
		ordering=['-pub_time']


class Tag(models.Model):
	tag=models.CharField(max_length=30,db_index=True,unique=True)
	pub_time=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.tag

	class Meta:
		ordering=['-pub_time']
				

class Blog(models.Model):
	title=models.CharField(u'标题',max_length=100)
	head_pic_url=models.CharField(u'头图链接',max_length=250,null=True,blank=True)
	pub_time=models.DateTimeField(auto_now=True)
	brief=models.CharField(u'摘要',max_length=200,blank=True,null=True)
	content=UEditorField(u'正文',width=900,height=600,toolbars="full",imagePath="",settings={})
	page_views=models.PositiveIntegerField(u'阅读量',default=0,editable=False)
	category1=models.ForeignKey(u'一级目录',Category1)
	category2=models.ForeignKey(u'二级目录',Category2,null=True)
	tags=models.ManyToManyField(u'标签',Tag,blank=True)
	def __unicode__(self):
		return self.title

	class Meta:
		ordering=['-pub_time']
		




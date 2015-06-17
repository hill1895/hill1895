from django.db import models
from DjangoUeditor.models import UEditorField

class Blog(models.Model):
	title=models.CharField(max_length=100)
	content=UEditorField(u'content',width=600,height=300,toolbars="full",imagePath="",settings={})
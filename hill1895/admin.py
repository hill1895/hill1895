from django.contrib import admin
from hill1895.models import Blog,Category1,Category2,Tag,Profile,Profile_Tag,Friend,Friend_Tag

class BlogAdmin(admin.ModelAdmin):
	list_display=('title','pub_time','category1','category2','page_views')
	serch_field=('category1','category2')
	list_filter=('category1','category2')

class Category1Admin(admin.ModelAdmin):
	list_display=('category_1',)

class Category2Admin(admin.ModelAdmin):
	list_display=('category_2',)		
	
class ProfileAdmin(admin.ModelAdmin):
	list_display=('title','pub_time')

class FriendAdmin(admin.ModelAdmin):
	list_display=('name','friend_url')


admin.site.register(Blog,BlogAdmin)
admin.site.register(Category1,Category1Admin)
admin.site.register(Category2,Category2Admin)
admin.site.register(Tag)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Profile_Tag)
admin.site.register(Friend,FriendAdmin)
admin.site.register(Friend_Tag)
# Register your models here.

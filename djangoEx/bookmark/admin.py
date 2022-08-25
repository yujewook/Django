from django.contrib import admin

# Register your models here.
from bookmark.models import Bookmark
#이미 만들어진 테이블을 admin 에게 뿌려라
class BookmarkAdmin (admin.ModelAdmin):
    #튜플로 만들어준다.
    list_display = ("title","url")
#admin 사이트에 등록해라 어드민에서 보여라 
admin.site.register(Bookmark, BookmarkAdmin) #이거를 통해서 사이트에 보여주는것

#url mapping 해주기

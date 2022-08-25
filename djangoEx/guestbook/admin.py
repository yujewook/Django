from django.contrib import admin
from guestbook.models import Guestbook

# Register your models here.
class GuestbookAdmin (admin.ModelAdmin):
    #보여줄 디비에서 어드민에게 보여 줄것 설정
    list_diplay = ("name","email","passwd","content")

#등록하기
                # modles에 있는 Guestbook
                                #현재 페이지 class GuestbookAdmin
admin.site.register( Guestbook ,GuestbookAdmin)


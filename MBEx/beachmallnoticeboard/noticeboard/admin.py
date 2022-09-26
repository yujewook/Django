from django.contrib import admin
from noticeboard.models import NoticeBoard

# Register your models here.
class NoticeBoardAdmin (admin.ModelAdmin):
    list_display=("noticenum","admin","noticetitle"
                 ,"content","noticedate" )
    
admin.site.register(NoticeBoard,NoticeBoardAdmin)
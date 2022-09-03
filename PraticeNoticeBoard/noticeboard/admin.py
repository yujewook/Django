from django.contrib import admin
from noticeboard.models import QnaBoard

# Register your models here.
class NoticeBoardAdmin(admin.ModelAdmin):
    list_display=("noticenum","adminid","noticetitle","content","noticedate")
admin.site.register(QnaBoard , NoticeBoardAdmin)
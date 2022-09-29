from django.contrib import admin
from qnaboard.models import Qnaboard

# Register your models here.
class QnaboardAdmin( admin.ModelAdmin ) :
    list_display = ( "qnanum", "userid", "qnatitle", "passwd", "qnacontent",
                     "reply_title","reply_content" )
admin.site.register( Qnaboard, QnaboardAdmin )
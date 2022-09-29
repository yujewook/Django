from django.db import models


# Create your models here.
class Qnaboard( models.Model ) :
    qnanum = models.AutoField( verbose_name="글번호", primary_key=True ) #
    userid = models.CharField( max_length=20, verbose_name="작성자", null=False ) #
    qnatitle = models.CharField( max_length=1000, verbose_name="글제목", null=False ) #
    passwd = models.CharField( max_length=20, verbose_name="비밀번호", null=False )
    qnacontent = models.CharField( max_length=6000, verbose_name="글내용", null=False ) #
    qnascore = models.IntegerField( verbose_name="조회수", default=0, null=False ) #
    ref = models.IntegerField( verbose_name="그룹화 아이디" )
    restep = models.IntegerField( verbose_name="글순서" )
    relevel = models.IntegerField( verbose_name="글레벨" )
    qnadate = models.DateTimeField( auto_now_add=True, verbose_name="작성일", blank=True, null=False ) #
    qnaip = models.CharField( max_length=15, verbose_name="아이피", null=False )##
    reply_order = models.CharField( max_length=15, verbose_name="댓글순서" ) #
    reply_depth = models.CharField( max_length=15, verbose_name="댓글깊이" ) #
    reply_number = models.CharField( max_length=15, verbose_name="댓글번호" )
    reply_title= models.CharField( max_length=1000, verbose_name="댓글제목")#
    reply_content = models.CharField( max_length=6000, verbose_name="관리자 댓글" )
    
    

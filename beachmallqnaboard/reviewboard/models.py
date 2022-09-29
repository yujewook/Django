from django.db import models

# Create your models here.
class Reviewboard( models.Model ) :
    reviewnum = models.AutoField( verbose_name="글번호", primary_key=True, null=False ) #
    prodnum = models.IntegerField( verbose_name="상품번호", null=False )
    reviewdate = models.DateTimeField( auto_now_add=True, verbose_name="작성일", blank=True, null=False )
    userid = models.CharField( max_length=20, verbose_name="작성자", null=False )
    reviewtitle = models.CharField( max_length=1000, verbose_name="글제목", null=False )
    reviewcontent = models.CharField( max_length=1000, verbose_name="글내용", null=False )
    reviewip = models.CharField( max_length=15, verbose_name="아이피", null=False )
    
    
    
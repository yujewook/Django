from django.db import models

# Create your models here.
class QnaBoard(models.Model):
                        #admin에서 보여주는것
    noticenum = models.AutoField(verbose_name="공지사항 글번호", primary_key=True) #자동증가
    adminid = models.CharField(max_length=20,verbose_name="작성자",null=False)
    noticetitle = models.CharField(max_length=1000,verbose_name="공지사항 글번호",null=False)
    content = models.CharField(max_length=6000,verbose_name="글내용",null=False) 
    restep =models.IntegerField(verbose_name="글순서") 
    noticedate =models.DateTimeField(auto_now_add=True,verbose_name="작성일",blank=True)
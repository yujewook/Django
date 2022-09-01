from django.db import models

# Create your models here.
class Board(models.Model):
                        #admin에서 보여주는것
    num = models.AutoField(verbose_name="글번호", primary_key=True) #자동증가
    writer = models.CharField(max_length=30,verbose_name="작성자",null=False)
    subject = models.CharField(max_length=300,verbose_name="글제목",null=False)
    passwd = models.CharField(max_length=20,verbose_name="비밀번호",null=False) 
    content = models.CharField(max_length=2000,verbose_name="글내용",null=False) 
    readcount = models.IntegerField(verbose_name="조회수",default=0)
    ref = models.IntegerField(verbose_name="그룹화 아이디")
    restep =models.IntegerField(verbose_name="글순서") 
    relevel =models.IntegerField(verbose_name="글레벨")
    regdate =models.DateTimeField(auto_now_add=True,verbose_name="작성일",blank=True)
    ip = models.CharField(max_length=30,verbose_name="아이피") 
    

class ImageBoard(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='imeages')
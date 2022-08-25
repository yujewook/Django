from django.db import models

# Create your models here.
#survey db 즉 테이블 만들어준다
class Survey(models.Model):
    #관리자가 관리하는 디비
    #   survey 아이디          자동인식증가
    survey_idx  = models.AutoField(primary_key=True)
    #질문
    question = models.TextField(null=False)
    #답변이 들어갈 컬럼
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
   
    status = models.CharField(max_length=1 , default="y")
    
#응답 디비
class Answer( models.Model):
     answer_idx  = models.AutoField(primary_key=True)
     #survey한 아이디 저장할곳 조인 할곳 위에 테이블과
     survey_idx  = models.IntegerField()
     #응답한것 답변 저장할 곳
     num = models.IntegerField()   
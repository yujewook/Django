from django.db import models

# Create your models here.
# 클래스를 테이블처럼 만들어 준다. sqlite db 테이블 만들고는 것 
                # modles 모듈안 Modle클래스를 임포트
class Bookmark (models.Model):
    title = models.CharField (max_length=100, blank = True , null=True)
    url = models.URLField( "url" , unique = True) #cmd에서 make migrate 사용한다 그러면 디비가 생성되고 db.sqlite가 생긴다.
    def __str__(self):  
        return self.title
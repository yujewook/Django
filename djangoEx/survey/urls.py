#survey url 매핑 받는곳
from survey import views
from django.urls.conf import path, re_path
urlpatterns = [
    #정규표현식으로 매핑 연결
    re_path(r"^main$" , views.main , name="main"), 
    #path( "main" , views.main, name="main"),
    # 저장 할때 연결해 줄것 
    path("save" , views.save, name="save"),
    #확인
    path("result", views.result, name="result")
]
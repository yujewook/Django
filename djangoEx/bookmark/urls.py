from django.urls.conf import path
from bookmark import views

#localhost:8000/bookmark/home  views.home이 실행한다.
urlpatterns =[
        #views안에 있는 
    path("home", views.home , name="home") 
    ]
from django.shortcuts import render
from django.template import loader
from bookmark.models import Bookmark
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    template = loader.get_template("home.html") # 템플릿 페이지 지정
    #Bookmark클래스
                #타이틀을 갖고온다.
    urllist = Bookmark.objects.order_by("title")
    # 갯수를 갖고와라 디비에서 갖고와라
    urlcount = Bookmark.objects.all().count()
    
    #보여주는 템플릿에 보내주는것
    context= {
        "urllist" : urllist,
        "urlcount" : urlcount,
        }
                                        #context를 넘겨라
    return HttpResponse(template.render( context, request)) 
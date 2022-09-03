from django.shortcuts import render
from django.views.generic.base import View
from django.template import loader
from noticeboard.models import QnaBoard
from django.http.response import HttpResponse

PAGE_SIZE=5
PAGE_BLOCK=5

# Create your views here.
class ListView(View):
    def get(self, request):
        template = loader.get_template( "notice.html" )
        count = QnaBoard.objects.all().count()
        pagenum = request.GET.get("pagenum")
        
        if not pagenum :
            pagenum = "1"
        pagenum = int(pagenum)
        # 밑에 바에서 보이는 것
        start = (pagenum - 1 ) *int(PAGE_SIZE) #(5-1)*10 +1 ->41
        end = start+ int(PAGE_SIZE)
        if end > count:
            end = count
            #전체글 다나옴 리스트로                 슬라이싱 0부터시작 하기 때문에 
        dtos = QnaBoard.objects.order_by("restep")[start:end]
        number = count - (pagenum-1)*int(PAGE_SIZE)
        
        #페이지에 글 보여주게 하는것
        startpage = pagenum// int(PAGE_BLOCK) * int(PAGE_BLOCK) +1 
        if pagenum % int(PAGE_BLOCK) == 0:
            startpage -= int(PAGE_BLOCK)-1
        endpage =   startpage + int(PAGE_BLOCK) -1
        pagecount = count // int(PAGE_SIZE)
        if count % int(PAGE_SIZE)>0:
            pagecount +=1
        if endpage>pagecount :
            endpage = pagecount    
        pages = range(startpage , endpage+1)
        context ={
            "count":count,
            "dtos": dtos,
            "pagenum" : pagenum,
            "number":number,
            "pages":pages,
            "startpage":startpage,
            "endpage":endpage,
            "pageblock":PAGE_BLOCK,
            "pagecount":pagecount,            
            }
        
        return HttpResponse(template.render(context, request))
    def post(self):
        pass
    
class ListDeatail(View):
    def get(self, request):
        noticenum = request.GET["noticenum"]
        pagenum = request.GET["pagenum"]
        number = request.GET["number"]
        dto = QnaBoard.objects.get(noticenum=noticenum)
        context={
            "noticenum":noticenum,
            "pagenum":pagenum,
            "number":number,
            "dto":dto,
            }
        template = loader.get_template("detailnotice.html")
        return HttpResponse(template.render(context,request))
    
    def post(self,request):
        pass
    
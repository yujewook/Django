from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse
from board.models import Board, ImageBoard
import logging
from django.utils.dateformat import DateFormat
from datetime import datetime
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
logger = logging.getLogger( __name__ )
#페이지 번호를 보이기 위한 변수
PAGE_SIZE = 5
PAGE_BLOCK = 3
class ModifyproView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return super( ModifyproView,self ).dispatch( request, *args, **kwargs)
    def get(self,request):
        pass
    def post(self, request):
        num = request.POST["num"]
        pagenum = request.POST["pagenum"]
        dto = Board.objects.get(num=num)
        dto.subject = request.POST["subject"]
        dto.content = request.POST["content"]
        dto.passwd = request.POST["passwd"]
        dto.save()
        
        return redirect("board:list")
        
        
        
class ModifyView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return super( ModifyView,self ).dispatch( request, *args, **kwargs)
    def get(self,request): #비밀번호 입력페이지로 넘어간다.
        num = request.GET["num"]
        pagenum = request.GET["pagenum"]
        context = {
            "num":num,
            "pagenum":pagenum
            }
        template = loader.get_template("modifyarticle.html")
        return HttpResponse(template.render(context, request))
    
    def post(self,request):
        num = request.POST["num"]
        pagenum = request.POST["pagenum"]
        passwd = request.POST["passwd"]
        dto = Board.objects.get(num=num)
        if ( passwd == dto.passwd ) :
            template = loader.get_template("modifytproarticle.html")
            context = {
                "num":num,
                "pagenum":pagenum,
                "dto":dto
                }
            return HttpResponse(template.render(context,request)) 
        else:
            template = loader.get_template("modifyarticle.html")
            context={
                "num":num,
                "pagenum":pagenum,
                "message":"비밀번호가 다릅니다."
                }
            return HttpResponse(template.render(context,request))
        
            
class DeleteView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return super( DeleteView,self ).dispatch( request, *args, **kwargs)
    def get(self,request):
        num = request.GET["num"]
        pagenum = request.GET["pagenum"]
        template = loader.get_template("deletearticle.html")
        context ={
            "num" : num,
            "pagenum" : pagenum
            }
        return HttpResponse(template.render(context,request))
    
    def post(self,request):
        num = request.POST["num"]
        pagenum = request.POST["pagenum"]
        passwd = request.POST["passwd"]
        #댓글 확인
        dto = Board.objects.get(num=num)
        
        if passwd == dto.passwd :
            
        #비밀번호가 같다                    
                                #같은 그룹이면서
            res = Board.objects.filter( ref__exact = dto.ref ).filter(restep__exact=dto.restep+1).filter(relevel__gt=dto.relevel)
            logger.info( res )
            if len(res) == 0 : #댓글이 없는경우 삭제한다
                
                dto.delete()
                
            else: #댓글이 있는 경우 삭제를 못하고 다시 list.html을 쓴다
                dto.readcount = -1
                dto.save()
            
            return redirect("board:list")
        #비밀번호가 다르다
        else:
            template = loader.get_template("deletearticle.html")
            #다시위에 있는것을 넘겨여 한다.
            context ={
                "num":num,
                "pagenum":pagenum,
                "message":"비밀번호가 다릅니다.",
                }
            
            
        return HttpResponse(template.render(context,request))
         
class DetailView(View):
    def get(self, request):
        num = request.GET["num"]
        pagenum = request.GET["pagenum"]
        number = request.GET["number"]
        dto = Board.objects.get(num=num)
        if dto.ip !=request.META.get("REMOTE_ADDR"):
            dto.readcount +=1
            dto.save()
        context={
            "num":num,
            "pagenum":pagenum,
            "number":number,
            "dto":dto,
            }
        template = loader.get_template("detailarticle.html")
        return HttpResponse(template.render(context,request))
    
    def post(self,request):
        pass




class WriteView( View ) :
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return super( WriteView,self ).dispatch( request, *args, **kwargs)
    def get(self, request ) :
        ref = 1
        restep = 0
        relevel = 0
        #num = request.GET["num"] # 우리가 직접 예외처리할 것이므로 이거 사용
        num = request.GET.get( "num" ) # 예외가 자동으로 처리됨
        if num == None :
            # 제목글
            try :
                # 글이 있는 경우
                maxnum = Board.objects.order_by( "-num" ).values()[0]["num"] #내림차순으로 (num)정렬하고 values로 한줄짜리 num값을 가져옴
                ref = maxnum + 1        # 그룹화아이디 = 글번호최대값 + 1 
            except IndexError :
                # 글이 없는 경우
                ref = 1
        else :
            # 답변글                # get 방식으로 데이터를 넘겨줌
            ref = request.GET["ref"]
            restep = request.GET["restep"]
            relevel = request.GET["relevel"]
            res = Board.objects.filter( ref__exact=ref ).filter( restep__gt=restep ) #필터 두개를 못쓴다
            for re in res : 
                re.restep = int( re.restep ) + 1 # 이미 있는 글이라서 db에 업데이트 해줘야 함 #re.restep 자료형이 명시가 안되서 에러날수있음 정수형처리함
                re.save() #업데이트
            restep = int( restep ) + 1  # 자료형이 애매해서 int로 형변환
            relevel = int( relevel ) + 1
            
        template = loader.get_template( "writearticle.html" )
        context = {
            "num" : num,
            "ref" : ref,
            "restep" : restep,
            "relevel" : relevel,
            }
        return HttpResponse( template.render( context, request ) )
    def post(self, request ) :
        dto = Board(
            writer = request.POST["writer"],
            subject = request.POST["subject"],
            passwd = request.POST["passwd"],
            content = request.POST["content"],
            readcount=0, #글쓸때 조회수는 0
            ref = request.POST["ref"], # 강제로 넘어오게 만듬
            restep = request.POST["restep"], # 강제로 넘어오게 만듬
            relevel = request.POST["relevel"], # 히든으로 만듬
            regdate = DateFormat( datetime.now() ).format( "Ymd" ),
            ip = request.META.get( "REMOTE_ADDR" )
            )
        dto.save()
        return redirect( "board:list" ) #app name 설정 때문에 board:list 로 해야함


class ListView( View ) :
    def get(self, request ) :
        template = loader.get_template( "list.html" )
        count = Board.objects.all().count()
        
        pagenum = request.GET.get("pagenum")
        if not pagenum :
            pagenum = "1"
        pagenum = int(pagenum)
        
        # 밑에 바에서 보이는 것
        start = (pagenum - 1 ) *int(PAGE_SIZE) #(5-1)*10 +1 ->41
        end = start+ int(PAGE_SIZE)
        
        if end>count:
            end = count
            #전체글 다나옴 리스트로                         슬라이싱 0부터시작 하기 때문에 
        dtos = Board.objects.order_by("-ref","restep")[start:end]
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
        context = {
            "count" : count,
            "dtos" : dtos,
            "pagenum" : pagenum,
            "number":number,
            "pages":pages,
            "startpage":startpage,
            "endpage":endpage,
            "pageblock":PAGE_BLOCK,
            "pagecount":pagecount,
            }
        return HttpResponse( template.render( context, request ) )
    def post(self, request ) :
        pass
    
    
    
    
class ImageView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return super( ImageView,self ).dispatch( request, *args, **kwargs)
    def get(self,request):
        template = loader.get_template("imageupload.html")
        context={}
        return HttpResponse(template.render(context,request))
            
    def post(self,request):    
        title= request.POST["title"]
        img = request.FILES["photo"]
        dto = ImageBoard(
            title = title,
            photo = img,
            )
        dto.save()
        #                url자리
        return redirect("board:imagedown")
    
    
    
class ImageDown(View):
    def get(self,request):
        template = loader.get_template("imagedown.html")
        dtos = ImageBoard.objects.all()
        context={
            "dtos":dtos
            }
        return HttpResponse(template.render(context,request))
    def post(self,request):
        pass
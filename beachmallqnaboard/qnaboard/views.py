from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse
from qnaboard.models import Qnaboard
import logging
from django.utils.dateformat import DateFormat
from datetime import datetime
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
logger = logging.getLogger( __name__ )

PAGE_SIZE = 5
PAGE_BLOCK = 3

class ListView( View ) :
    def get(self, request ) :
        template = loader.get_template( "list.html" )
        count = Qnaboard.objects.all().count()
        
        pagenum = request.GET.get( "pagenum" )
        if not pagenum :
            pagenum = "1"
        pagenum = int( pagenum )
        
        start = ( pagenum - 1 ) * int(PAGE_SIZE)          # ( 5 - 1 ) * 10 + 1     41
        end = start + int(PAGE_SIZE)                      # 41 + 10 - 1            50
        if end > count :
            end = count
        dtos = Qnaboard.objects.order_by( "-ref", "restep" )[start:end] # jsp와 다르게 슬라이싱해서 씀
        number = count - ( pagenum - 1 ) * int(PAGE_SIZE )
        
        startpage = pagenum // int(PAGE_BLOCK) * int(PAGE_BLOCK) + 1       # 9 // 10 * 10 + 1    1
        if pagenum % int(PAGE_BLOCK) == 0:
            startpage -= int(PAGE_BLOCK)
        endpage = startpage + int(PAGE_BLOCK) - 1                         # 1 + 10 -1           10
        pagecount = count // int(PAGE_SIZE)
        if count % int(PAGE_SIZE) > 0 :
            pagecount += 1
        if endpage > pagecount :
            endpage = pagecount
        pages = range( startpage, endpage+1 )
        context = {
            "count" : count,
            "dtos" : dtos,
            "pagenum" : pagenum,
            "number" : number,
            "pages" : pages,
            "startpage" : startpage,
            "endpage" : endpage,
            "pageblock" : PAGE_BLOCK,
            "pagecount" : pagecount,
            }
        return HttpResponse( template.render( context, request ) )
    def post(self, request ) :
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
        qnanum = request.GET.get( "qnanum" ) # 예외가 자동으로 처리됨
        if qnanum == None :
            # 제목글
            try :
                # 글이 있는 경우
                maxnum = Qnaboard.objects.order_by( "-qnanum" ).values()[0]["qnanum"] #내림차순으로 정렬하고 values로 한줄짜리 num값을 가져옴
                ref = maxnum + 1        # 그룹화아이디 = 글번호최대값 + 1 
            except IndexError :
                # 글이 없는 경우
                ref = 1
        else :
            # 답변글                # get 방식으로 데이터를 넘겨줌
            ref = request.GET["ref"]
            restep = request.GET["restep"]
            relevel = request.GET["relevel"]
            res = Qnaboard.objects.filter( ref__exact=ref ).filter( restep__gt=restep ) # __gt는 크다라는 의미
            for re in res : 
                re.restep = int( re.restep ) + 1 # 이미 있는 글이라서 db에 업데이트 해줘야 함 #re.restep 자료형이 명시가 안되서 에러날수있음 정수형처리함
                re.save() #업데이트
            restep = int( restep ) + 1  # 자료형이 애매해서 int로 형변환
            relevel = int( relevel ) + 1
            
        template = loader.get_template( "writearticle.html" )
        context = {
            "qnanum" : qnanum,
            "ref" : ref,
            "restep" : restep,
            "relevel" : relevel,
            }
        return HttpResponse( template.render( context, request ) )
    def post(self, request ) :
        dto = Qnaboard(
            userid = request.POST["userid"],
            qnatitle = request.POST["qnatitle"],
            passwd = request.POST["passwd"],
            qnacontent = request.POST["qnacontent"],
            qnascore=0, #글쓸때 조회수는 0
            ref = request.POST["ref"], # 강제로 넘어오게 만듬
            restep = request.POST["restep"], # 강제로 넘어오게 만듬
            relevel = request.POST["relevel"], # 히든으로 만듬
            qnadate = DateFormat( datetime.now() ).format( "Ymd" ),
            qnaip = request.META.get( "REMOTE_ADDR" )
            )
        dto.save()
        return redirect( "qnaboard:list" ) #app name 설정 때문에 board:list 로 해야함
    
class DetailView( View ) :
    def get(self, request ) :
        qnanum = request.GET["qnanum"]
        pagenum = request.GET["pagenum"]
        number = request.GET["number"]
        dto = Qnaboard.objects.get( qnanum = qnanum )
        if dto.qnaip != request.META.get( "REMOTE_ADDR" ) :
            dto.qnascore += 1
            dto.save()
        context = {
            "qnanum" : qnanum,
            "pagenum" : pagenum,
            "number" : number,
            "dto" : dto,
            }
        template = loader.get_template( "detailarticle.html" )
        return HttpResponse( template.render( context, request ) )
        
    def post(self, request ) :
        pass
    
class DeleteView( View ) :
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return super( DeleteView,self ).dispatch( request, *args, **kwargs)
    
    def get(self, request ) :
        qnanum = request.GET["qnanum"]
        pagenum = request.GET["pagenum"]
        template = loader.get_template( "deletearticle.html" )
        context = {
            "qnanum" : qnanum,
            "pagenum" : pagenum,
            }
        
        return HttpResponse( template.render( context, request ) )
             
    def post(self, request ) :
        qnanum = request.POST["qnanum"]
        pagenum = request.POST["pagenum"]
        passwd = request.POST["passwd"]
        dto = Qnaboard.objects.get( qnanum = qnanum )
        
        if passwd == dto.passwd :
            # 비밀번호가 같다
            res = Qnaboard.objects.filter( ref__exact=dto.ref ).filter( restep__exact=dto.restep+1 ).filter( relevel__gt=dto.relevel )
            logger.info( res )
            if len( res ) == 0 :
                # 댓글이 없는 경우 삭제
                dto.delete()
            else :
                # 댓글이 있는 경우
                dto.qnascore = -1
                dto.save()
            return redirect( "qnaboard:list" )
        else :
            # 비밀번호가 다르다
            template = loader.get_template( "deletearticle.html" )
            context = {
                "qnanum" : qnanum,
                "pagenum" : pagenum,
                "message" : "비밀번호가 다름 뭔지다시 확인",
                }
            return HttpResponse( template.render( context, request ) )
        
class ModifyView( View ) :
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return super( ModifyView,self ).dispatch( request, *args, **kwargs)
    
    def get(self, request ) :
        qnanum = request.GET["qnanum"]
        pagenum = request.GET["pagenum"]
        context = {
            "qnanum" : qnanum,
            "pagenum" : pagenum,
            }
        template = loader.get_template( "modifyarticle.html" )
        return HttpResponse( template.render( context, request ) )
    
    def post(self, request ) :
        qnanum = request.POST["qnanum"]
        pagenum = request.POST["pagenum"]
        passwd = request.POST["passwd"]
        dto = Qnaboard.objects.get( qnanum = qnanum )
        if( passwd == dto.passwd ) :
            template = loader.get_template( "modifyproarticle.html" )
            context = {
                "qnanum" : qnanum,
                "pagenum" : pagenum,
                "dto" : dto,
                }
            return HttpResponse( template.render( context, request ) )
            
        else :
            template = loader.get_template( "modifyarticle.html" )
            context = {
                "qnanum" : qnanum,
                "pagenum" : pagenum,
                "message" : "비밀번호가 다릅니다",
                }
            return HttpResponse( template.render( context, request ) )

class ModifyProView( View ) :
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return super( ModifyProView,self ).dispatch( request, *args, **kwargs)
    def get(self, request ) :
        pass
    def post(self, request) : # post만 구현하면 된다
        qnanum = request.POST["qnanum"]
        pagenum = request.POST["pagenum"]
        dto = Qnaboard.objects.get( qnanum = qnanum ) 
        dto.qnatitle = request.POST["qnatitle"]
        dto.qnacontent = request.POST["qnacontent"]
        dto.passwd = request.POST["passwd"]
        dto.save()
        return redirect( "qnaboard:list" )
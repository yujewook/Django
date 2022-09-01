from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse

import logging

from django.utils.dateformat import DateFormat
from member.models import Member
from datetime import datetime
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django import template


logger = logging.getLogger(__name__)
# Create your views here.
class ModifyProView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ModifyProView, self).dispatch(request , *args, **kwargs)
    #여기에는 get방식이 없다.
    def get(self, request):
        pass
    def post(self, request):
        id = request.session.get("memid")
        dto = Member.objects.get(id=id)
        dto.passwd = request.POST["passwd"]
        dto.email = request.POST["email"]
        tel1 =request.POST["tel1"]
        tel2 = request.POST["tel2"]
        tel3 = request.POST["tel3"]
        if tel1 and tel2 and tel3 :
            tel = tel1+"-"+tel2+"-"+tel3
        dto.tel =tel
        dto.save() #insert된다
        return redirect("main")
        
        
class ModifyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ModifyView, self).dispatch(request , *args, **kwargs)
    
    def get(self, request):
        template = loader.get_template("modify.html")
        context={}
        return HttpResponse(template.render(context,request))
    def post(self, request):
        id = request.session.get("memid")
        passwd = request.POST["passwd"]
        dto = Member.objects.get(id=id)
        
        if passwd == dto.passwd:
            template = loader.get_template("modifypro.html")
            #여기서 또 짤라준다 dto를 잘라서 template에서 사용하게 만들어준다
            if dto.tel :
                t = dto.tel.split("-")
                context = {
                    "dto" : dto,
                    "t" : t
                    }
            else:
                context={
                    "dto" : dto
                    }
        else: 
            template=loader.get_template("modify.html")
            context={
                "message" : "비밀번호가 다릅니다." 
                }   
        return HttpResponse(template.render(context,request))    
            
class DeleteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(DeleteView, self).dispatch(request , *args, **kwargs)
    #get방식일때는 페이지만 넘기고 
    def get(self , request):
        template = loader.get_template("delete.html")
        context={}
        return HttpResponse(template.render(context,request))
    #post방식에서 유효성 검사를 해준다.
    def post(self , request):
        id = request.session.get("memid")
        passwd = request.POST["passwd"]
        dto = Member.objects.get(id=id)
        if passwd == dto.passwd :
            dto.delete()                  # db지우기
            del(request.session["memid"]) #로그아웃상태로 만들기
            return redirect("main")
        else: 
            template = loader.get_template("delete.html")
            context={
                "message" : "비밀번호가 다릅니다."
             
                }
            return HttpResponse(template.render(context, request))
        
        
class LogoutView(View):
    def get(self, request):
        del(request.session["memid"])
        return redirect("main")
    
    def post(self, request):
        pass
         

class MainView(View):
    def get(self, request):
        memid = request.session.get("memid")
        if memid:
            context ={
                "memid":memid,
                }
        else:
            context={}
        template=loader.get_template("main.html")
        return HttpResponse(template.render(context,request))    
    def post(self,request):
        pass
    
class LoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request , *args, **kwargs)
    
    def get(self,request):
        tempalte= loader.get_template("login.html")
        context={
            }
        return HttpResponse(tempalte.render(context,request))
    
    def post(self, request):
        id = request.POST["id"]
        passwd = request.POST["passwd"]
        
        try:
            dto = Member.objects.get(id=id)
            if passwd == dto.passwd:
                request.session["memid"] = id 
                message ="회원입니다."
                return redirect("main")
            else: 
                message = "비밀번호가 다릅니다."
        except ObjectDoesNotExist :
            message = "아이디가 없습니다."
        template= loader.get_template("login.html")
        
        context = {
            "message" :message
            }
        return HttpResponse(template.render(context, request))

    
class ConfirmView(View):
    def get(self, request):
        id = request.GET["id"]  
        result = 0
        try :  
            Member.objects.get(id=id)
            result = 1
        except ObjectDoesNotExist :
            result = 0
        context= {
             "result" : result,
             "id" : id
            }
        #아이디 넣을때 마다 저장하게 log 저장
        logger.info("id : " + id)
        template =loader.get_template("confirm.html")
        return HttpResponse( template.render(context, request))
    
    def post(self, request):  
        pass


class WriteView(View):
    #csrf 처리하기위한 것
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WriteView, self).dispatch(request , *args, **kwargs)
    
    # get방식 버튼을 입력할때
    def get(self,request):
        template = loader.get_template("write.html")
        context={
            }
        return HttpResponse(template.render(context,request))
    #입력 데이터 받는곳    
    def post(self,request):
        tel = ""
        tel1 = request.POST["tel1"]
        tel2 = request.POST["tel2"]
        tel3 = request.POST["tel3"]
        if tel1 and tel2 and tel3 :
            tel = tel1  + "-" + tel2 + "-" + tel3
        
        
        #id = request.POST["id"] 로 밖으로 해야한다. dto안에있는건 객체로 되기 때문에..but str(id)
        #라고한다
        dto = Member(
           id = request.POST["id"],
           passwd = request.POST["passwd"],
           name = request.POST["name"],
           email = request.POST["email"],
           # 짤라받는곳 붙여 받기
           tel = tel,
           depart = request.POST["depart"],
           logtime = DateFormat(datetime.now()).format("Y-m-d") 
        )
        dto.save()
        #setting에서 info 에다 쌓이는것 
        #문자열 하나만 넘어가게 되어있는 것이다. , 말고 + 로해야한다. str(id)로 들어간다.-> 안되서 밑으 방법으로 
        #logger.info("write : " + request.POST["id"]) ->하면 로거가 쌓이는 방법
        logger.info( "write :" + dto.id )
        return redirect("login")
    
























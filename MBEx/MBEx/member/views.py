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

logger = logging.getLogger(__name__)
# Create your views here.
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
        logger.info("id" + id)
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
        #문자열 하나만 넘어가게 되어있는 것이다.
        logger.info( "write :" + id )
        return redirect("login")
    

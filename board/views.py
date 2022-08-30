from django.shortcuts import render
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse
from board.models import Board
import logging

logger = logging.getLogger(__name__)
# Create your views here.
class WriteView(View):
    def get(self,request):
        template = loader.get_template("writearticle.html")
        context={}
        return HttpResponse(template.render(context, request)) 
    
    def post(self,request):
        pass
    
    
class ListView(View):
    def get(self, request):
        template = loader.get_template("list.html")
        count = Board.objects.all().count() # 전체 갯수
        context={
            "count" : count, 
            }
        return HttpResponse(template.render(context,request))
    def post(self,request):
        pass
    
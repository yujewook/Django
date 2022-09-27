from django.shortcuts import render
from django.template import loader
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from survey.models import Survey, Answer
# Create your views here.
class SurveyView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return super( SurveyView,self ).dispatch( request, *args, **kwargs)
    def get(self,request):
        template = loader.get_template("survey.html")
        survey = Survey.objects.filter(status="y").order_by("-survey_idx")[0]
        context ={
                "survey" : survey
            }
        return HttpResponse(template.render(context,request))
    
    def post(self,request):
        template = loader.get_template("save.html")
        dto = Answer(survey_idx = request.POST["survey_idx"],
                      num = request.POST["num"],
                      num1 = request.POST["num1"],
                      num2 = request.POST["num2"],
                      num3 = request.POST["num3"],
                      num4 = request.POST["num4"],
                      #userId = request.POST["id"]
                      )
        dto.save()
        context={}
        return HttpResponse(template.render(context,request))
from django.shortcuts import render
from django.template import loader
from survey.models import Survey, Answer
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def main(request):
    #template 패키지안 main.html과 연결
    template = loader.get_template("main.html")
    #넘길 데이터 설정
    #최신 설문 하나만 갖고오기
        #Survey오브젝트에 있는 
       #db에서 select 같은것        진행중인 설문 yes인      역순- 다갖고 와라        맨위에꺼
    survey =Survey.objects.filter(status = "y").order_by("-survey_idx")[0]
    #context는 꼭 있어야 하고 survey java에서 setAttribute 같은 느낌
    context = {
        "survey" : survey,
        }
                                        #request에다가 보낸다
    return HttpResponse(template.render(context,request))

@csrf_exempt
def save(request):
    #main.html에서 name에 있던 survey_idx,num이 들어온다.
    template = loader.get_template("save.html")
    #                메인에서 포스트로 넘김 여기도 post
    dto = Answer(survey_idx = request.POST["survey_idx"], num = request.POST["num"])
    # save함수를 사용한다.
    dto.save()
    #이건 꼭있어야한다.
    context={}
    return HttpResponse(template.render(context,request))

def result(request):
    #결과를 받을 템플릿 페이지
    template = loader.get_template("result.html")
    survey_idx = request.GET["survey_idx"] # get방식으로 갖고온다. model에서 갖고온다.
    ans = Survey.objects.get(survey_idx = survey_idx ) #데이터를 꺼내 왔다.
    answer = [ans.ans1,ans.ans2,ans.ans3,ans.ans4]
    
    #여기에 sql을 써주면 된다. survey당 다르기 때문에 sql이 어렵다
    #select survey_idx,num,count(num)을 sum_num으로 부르겠다 결과 테이블로 만들겠다.
    #round (,1)를 rate로 부른다 결과 테이블
    surveylist = Survey.objects.raw("""
        select survey_idx,num,count(num) sum_num,
        round( (select count(*) from survey_answer where survey_idx=an.survey_idx and num=an.num )*100
        /(select count(*) from survey_answer where survey_idx=an.survey_idx) ,1) rate
        from survey_answer an
        where survey_idx=%s
        group by survey_idx, num""",survey_idx)
    
    surveylist = zip(surveylist,answer)
    context={
        "survey_idx" : survey_idx,
        "surveylist" : surveylist,
        }
    return HttpResponse(template.render(context,request))
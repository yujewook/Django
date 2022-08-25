from django.shortcuts import render, redirect
from guestbook.models import Guestbook
from django.http.response import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def list(request):
    template = loader.get_template("list.html")
    gbcount = Guestbook.objects.count()
    gblist = Guestbook.objects.order_by("-idx")
    
    context = {
         "gbcount" : gbcount ,
         "gblist" : gblist
        }
    
    return HttpResponse(template.render(context,request))

def write(request):
    template = loader.get_template("write.html")
    context={}
    return HttpResponse(template.render(context,request))

@csrf_exempt
def writepro(request):
            #생성자에 포스트로 받은거 포스트로 한다
    dto = Guestbook(
            #db이름              html이름
            name = request.POST["name"],
            email = request.POST["email"],
            passwd = request.POST["passwd"],
            content = request.POST["content"]
        )
    dto.save()
    #리스트로 넘어 가야해 따로 writepro.html가 없기 때문에 데이터를 넘겨주기때문에
    #gettemplate 할 필요가 없다
    #redirect를 사용한다 다시 url list으로 넘어간다
    return redirect("list")

@csrf_exempt
def passwdck (request):
    #비밀번호 맞을때 넘어가는 곳 만들기 html 연결해주기
    template = loader.get_template("edit.html")
    idx = request.POST["idx"]
    passwd = request.POST["passwd"]
    #db와 입력된 값 비교하기위해
    dto = Guestbook.objects.get(idx=idx)
    context={
        "dto" : dto
        }
    if passwd == dto.passwd :
        return HttpResponse(template.render(context,request))
    else:
        #url로 말해준다
        return redirect("list")
    
def delete(request):
    idx = request.GET["idx"]
    Guestbook.objects.get(idx=idx).delete()
    return redirect("list")

@csrf_exempt
def update(request):
    idx = request.POST["idx"]
    dto = Guestbook.objects.get(idx = idx)
    newdto = Guestbook(
        idx = dto.idx,
        name = dto.name,
        email = request.POST["email"],
        passwd = request.POST["passwd"],
        content = request.POST["content"]
        )
    # 같은 거 주면 update / save를하기 때문에
    newdto.save()
    return redirect("list")
    
    
    
    
    
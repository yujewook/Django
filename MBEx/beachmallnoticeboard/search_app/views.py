from django.shortcuts import render
from noticeboard.models import NoticeBoard
from django.db.models import Q


# Create your views here.
def searchResult(request):
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        dtos = NoticeBoard.objects.all().filter(
            Q(noticetitle__icontains=query)|
            Q(content__icontains=query)
        )
      
    
    return render(request,'search.html', {'query':query, 'dtos':dtos})    
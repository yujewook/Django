"""djangoEx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include


#어플 받을때 한번 설정해준다 매핑해준것
urlpatterns = [
    path('admin/', admin.site.urls), #http://localhost:8000/admin/ 치면 나오는 컨트롤러
    # "http://localhost:8000/bookrmark/에 들어오면 bookmark.urls를 이용해라
    path("bookmark/" , include("bookmark.urls")),
    #survey mapping
    path("survey/",include("survey.urls")),
    path("guestbook/",include("guestbook.urls"))
]
 
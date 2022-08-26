from django.urls.conf import path
from django.views.generic.base import TemplateView
urlpatterns=[
    path("main", TemplateView.as_view(template_name="main.html")) #view.py필요 없이 main.html에만 생성가능 
    
]
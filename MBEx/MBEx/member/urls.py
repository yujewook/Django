from django.urls.conf import path
from django.views.generic.base import TemplateView
from member import views

urlpatterns=[
    #path("main", TemplateView.as_view(template_name="main.html")), #view.py필요 없이 main.html에만 생성가능
    path("main", views.MainView.as_view(), name="main" ),  
    path("write", views.WriteView.as_view() ,name="write"),
    path("confirm", views.ConfirmView.as_view(), name="confirm"), 
    path("login", views.LoginView.as_view(), name="login"),
]
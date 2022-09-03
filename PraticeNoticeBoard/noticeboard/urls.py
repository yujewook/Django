from django.urls.conf import path
from noticeboard import views

urlpatterns=[
    path("list",views.ListView.as_view(), name="list"),
    path("listdetail",views.ListDeatail.as_view(), name="listdetail")
    ]

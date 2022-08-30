from django.urls.conf import path
from board import views

#하나하나 다해줘야 한다.
app_name="board"
#get방식으로만 넘어온다.
urlpatterns =[
    path("list", views.ListView.as_view() , name="list"),
    path("write", views.WriteView.as_view(), name="write")
] 

 
 
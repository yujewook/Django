from django.urls.conf import path
from board import views

#하나하나 다해줘야 한다.  같은 url = write을 구별해주기위해서 app_name  
app_name="board" 
#get방식으로만 넘어온다.
urlpatterns =[
    path("list", views.ListView.as_view() , name="list"),
    path("write", views.WriteView.as_view(), name="write"),
    path("detail",views.DetailView.as_view(), name="detail"),
    path("delete",views.DeleteView.as_view(), name="delete"),
    path("modify",views.ModifyView.as_view(), name="modify"),
    path("modifypro",views.ModifyproView.as_view(), name="modifypro"),
    path("image",views.ImageView.as_view(), name="image"),
    path("imagedown",views.ImageDown.as_view(),name="imagedown"),  
    
] 

 
 
 
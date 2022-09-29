from django.urls.conf import path
from qnaboard import views

app_name = "qnaboard"

urlpatterns = [
    path( "list", views.ListView.as_view(), name="list" ),
    path( "write", views.WriteView.as_view(), name="write" ),
    path( "detail", views.DetailView.as_view(), name="detail" ),
    path( "delete", views.DeleteView.as_view(), name="delete" ),
    path( "modify", views.ModifyView.as_view(), name="modify" ),
    path( "modifypro", views.ModifyProView.as_view(), name="modifypro" ),
    # path( "image", views.ImageView.as_view(), name="image"),
    # path( "imagedown", views.ImageDown.as_view(), name="imagedown" ),
    ]

 
 
    # 페이지들이 다 get방식으로 넘어온다 csrf토큰 잡을 필요도 없음
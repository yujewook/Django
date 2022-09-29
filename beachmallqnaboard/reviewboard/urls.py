from django.urls.conf import path
from reviewboard import views

app_name = "reviewboard"

urlpatterns = [
    # path( "image", views.ImageView.as_view(), name="image"),
    # path( "imagedown", views.ImageDown.as_view(), name="imagedown" ),
    ]

 
 
    # 페이지들이 다 get방식으로 넘어온다 csrf토큰 잡을 필요도 없음
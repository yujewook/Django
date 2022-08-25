from django.urls.conf import path
from guestbook import views

urlpatterns = [
    # views.main 이실행 되는 것 main으로 만들어 주기
    path("list" , views.list , name="list"),
    path("write", views.write, name="write"),
    path("writepro", views.writepro, name="writepro"), #데이터 넘겨서 저장만 받는곳
    path("passwdck", views.passwdck,name="passwdck"),
    path("delete",views.delete,name="delete"),
    path("update",views.update,name="update")

]


from django.urls import path
from survey import views


urlpatterns = [
    path("surveylist",views.SurveyView.as_view(),name="surveylist"),
]
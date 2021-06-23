#퀴즈 앱에 대한 url 관리
#myapi url과 연결하는 작업
from django.urls import path, include
from .views import helloAPI, randomQuiz

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>", randomQuiz),
]


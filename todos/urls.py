
from django.urls import path, include
from todos.views import TodoList, TodoDetail

urlpatterns = [
    path("", TodoList.as_view()),
    path("<int:pk>", TodoDetail.as_view())
]

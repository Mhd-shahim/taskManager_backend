from django.urls import path
from .views import createTask

urlpatterns = [
    path('/create-task',createTask.as_view(),name="create-task")
]
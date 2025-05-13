from django.urls import path
from .views import createTask, taskView, TaskDelete, EditTask

urlpatterns = [
    path('/create-task',createTask.as_view(),name="create-task"),
    path('/tasks', taskView.as_view(), name='all-tasks'),         
    path('/tasks/<int:id>', taskView.as_view(), name='task-detail'),
    path('/task-delete/<int:id>', TaskDelete.as_view(), name='task-delete'),
    path('/edit-task/<int:id>', EditTask.as_view(), name="edit-task")   
]
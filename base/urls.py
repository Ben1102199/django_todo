from django.urls import path
from .views import tasklist,Taskdetail,TaskCreateview,Task_Update, DeleteView

urlpatterns = [
    path('',tasklist.as_view(), name='tasks'),
    path('task/<int:pk>/',Taskdetail.as_view(), name='task'),
    path('task-create',TaskCreateview.as_view(), name='task-create'),
    path('task-update/<int:pk>/',Task_Update.as_view(), name='Task-update'),
    path('task-delete/<int:pk>/',DeleteView.as_view(), name='task-delete'),
]
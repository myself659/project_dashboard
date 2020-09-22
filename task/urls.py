from django.urls import path
from . import views
urlpatterns = [
   path('', views.home),
   path('task_list/', views.TaskListView.as_view(), name='task_list'),
   path('task_list/create', views.TaskCreateView.as_view(), name='task_create')
]
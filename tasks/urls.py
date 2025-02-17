from django.urls import path
from . import views
from tasks.views import custom_logout

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    path('logout/', custom_logout, name='logout')
]
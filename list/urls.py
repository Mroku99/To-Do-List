from django.urls import path
from django.contrib.auth import views as auth_view

from . import views

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.UserRegister.as_view(), name='register'),

    path('', views.TaskList.as_view(), name='task_list'),
    path('detail/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('create-task/', views.TaskCreate.as_view(), name='task_create'),
    path('edit-task/<int:pk>/', views.TaskEdit.as_view(), name='task_edit'),
    path('delete-task/<int:pk>/', views.TaskDelete.as_view(), name='task_delete'),
]

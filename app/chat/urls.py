from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chat'),
    path('user_chat/<int:receiver_id>/', views.user_chat, name='user_chat'),
    # path('create_user_chat/<int:receiver_id>/', views.create_user_chat, name='create_user_chat'),
    path('group_chat/<int:group_id>/', views.group_chat, name='group_chat'),
    path('create_group_chat/', views.create_group_chat, name='create_group_chat'),
]

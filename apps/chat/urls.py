from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('start/<int:item_id>/', views.start_chat, name='start_chat'),
    path('room/<int:room_id>/', views.chat_room, name='chat_room'),
    path('inbox/', views.inbox, name='inbox'),
]
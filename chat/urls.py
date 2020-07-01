from django.urls import path

from .views import (
    lobby,
    room,
    new_conversation,
    start_conversation,
)

urlpatterns = [
    path('', lobby, name='chat_home'),
    path('<conversation_uuid>/', room, name='room'),
    path('new/', new_conversation, name='new_conversation'),
    path('start/<participant_id>/', start_conversation, name='start_conversation'),
]
from django.urls import path

from chatrooms.views import Index, Room

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('chat/<str:room_name>/', Room.as_view(), name='room')
]


from django.urls import path
from .views import index

app_name = 'frontend'


urlpatterns = [
    path('', index),
    path('create', index),
    path('join', index),
    path('room/<str:roomCode>', index),
     path('info', index),
]
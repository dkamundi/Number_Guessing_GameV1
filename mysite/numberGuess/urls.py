from django.urls import path
from .views import register, login_view, play_game

# Import views from the application's views module

urlpatterns = [
    path('', register, name='register'),
    path('login/', login_view, name='login'),
    path('play/', play_game, name='play_game'),
]

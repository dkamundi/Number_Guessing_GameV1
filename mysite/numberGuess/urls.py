from django.urls import path
from .views import register, login_view, play_game

# Import views from the application's views module

urlpatterns = [
    # Define a URL pattern for the registration page, mapped to the 'register' view.
    path('', register, name='register'),
    
    # Define a URL pattern for the login page, mapped to the 'login_view' view.
    path('login/', login_view, name='login'),

    # Define a URL pattern for the game-playing page, mapped to the 'play_game' view.
    path('play/', play_game, name='play_game'),
]

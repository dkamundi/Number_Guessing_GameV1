from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm
from .models import GameSession
import random

# Import UserRegistrationForm and UserLoginForm from the forms module

from .forms import UserRegistrationForm, UserLoginForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'numberGuess/register.html', {'form': form})

# Registration view - handles user registration using UserRegistrationForm

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('play_game')
    else:
        form = UserLoginForm()
    return render(request, 'numberGuess/login.html', {'form': form})

# Login view - handles user login using UserLoginForm

@login_required
def play_game(request):
    game_session, created = GameSession.objects.get_or_create(user=request.user, is_active=True)
    if created:
        game_session.secret_number = random.randint(0, 100)
        game_session.save()

    feedback = ""
    
    if request.method == 'POST':
        guess = int(request.POST['guess'])
        game_session.guesses += 1
        game_session.attempts -= 1

        if guess < game_session.secret_number:
            feedback = "Your guess is too low!"
        elif guess > game_session.secret_number:
            feedback = "Your guess is too high!"
        elif guess == game_session.secret_number:
            feedback = "Congratulations! You guessed the correct number!"
            game_session.is_active = False
        elif game_session.attempts == 0:
            feedback = f"Sorry! You've used all your attempts. The correct number was {game_session.secret_number}."
            game_session.is_active = False

        game_session.save()

    return render(request, 'numberGuess/play_game.html', {'game_session': game_session, 'feedback': feedback})


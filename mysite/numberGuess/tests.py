from django.test import TestCase
from django.contrib.auth.models import User
from .models import GameSession
from .forms import UserRegistrationForm, UserLoginForm

class UserRegistrationTestCase(TestCase):
    def test_user_registration(self):
        # Create a test user
        user_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = UserRegistrationForm(data=user_data)
        self.assertTrue(form.is_valid())
        form.save()
        
        # Check if the user is created in the database
        user = User.objects.get(username='testuser')
        self.assertEqual(user.username, 'testuser')
        
class UserLoginTestCase(TestCase):
    def setUp(self):
        # Create a test user for login tests
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
    
    def test_user_login(self):
        # Attempt to log in the test user
        login_data = {
            'username': 'testuser',
            'password': 'testpassword123',
        }
        response = self.client.post('/login/', data=login_data)
        
        # Check if the login was successful
        self.assertEqual(response.status_code, 302)  # 302 is the HTTP status code for a successful redirect
        
class PlayGameTestCase(TestCase):
    def setUp(self):
        # Create a test user for the game session
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
    
    def test_play_game(self):
        # Log in the test user
        login_data = {
            'username': 'testuser',
            'password': 'testpassword123',
        }
        self.client.post('/login/', data=login_data)
        
        # Attempt to access the play_game view
        response = self.client.get('/play/')
        
        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)
        
        # Create a game session for the user
        game_session = GameSession.objects.get(user=self.user)
        
        # Test submitting a guess
        guess_data = {
            'guess': game_session.secret_number  # Submit the correct guess
        }
        response = self.client.post('/play/', data=guess_data)
        
        # Check if the response contains the success message
        self.assertContains(response, 'Congratulations! You guessed the correct number!')


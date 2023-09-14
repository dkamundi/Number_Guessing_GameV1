from django.db import models

# Define a Django model called GameSession
class GameSession(models.Model):
    # A foreign key relationship to the built-in User model in Django's authentication system.
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    # An integer field to store the secret number for the game (nullable, can be empty).
    secret_number = models.IntegerField(null=True)
    
    # An integer field to store the number of attempts allowed in the game (default is 10).
    attempts = models.IntegerField(default=10)
    
    # An integer field to store the number of guesses made by the user (default is 0).
    guesses = models.IntegerField(default=0)
    
    # A boolean field to indicate if the game session is currently active (default is True).
    is_active = models.BooleanField(default=True)
    
    # Define a human-readable string representation for a GameSession object.
    def __str__(self):
        return f"{self.user.username}'s game record"

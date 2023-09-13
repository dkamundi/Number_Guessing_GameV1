from django.db import models

class GameSession(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    secret_number = models.IntegerField(null=True)
    attempts = models.IntegerField(default=10)
    guesses = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username}'s game record"

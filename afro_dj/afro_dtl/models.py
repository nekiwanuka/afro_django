from django.db import models

# we are creating a custom user model here named "user_account"
class User_account(models.Model):
    username = models.CharField(max_length=22)
    gender = models.CharField(max_length=6)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=22)
    signup_time = models.DateTimeField(auto_now_add=True)
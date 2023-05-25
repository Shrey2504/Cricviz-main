from django.db import models
from django.contrib.auth.password_validation import validate_password


# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=50, validators=[validate_password], default='default_password')

    def __str__(self):
        return self.username

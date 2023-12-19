
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username=models.CharField(max_length=100)
    bio=models.CharField(max_length=100,default="Type Your biography")
   


    # You don't need to redefine 'username' here because AbstractUser already has it
    # If you want to make 'email' as the USERNAME_FIELD, use the 'USERNAME_FIELD' attribute

    USERNAME_FIELD = 'email'  # Set the USERNAME_FIELD to 'email'
    REQUIRED_FIELDS = ['username']  # 'username' is required, as it's not included in USERNAME_FIELD

    def __str__(self):
        return self.username

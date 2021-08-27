from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, null=False, blank=False)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18)])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'age']

    def __str__(self) -> str:
        return self.email
    
    def __repr__(self) -> str:
        return self.email
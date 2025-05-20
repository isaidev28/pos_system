from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('vendedor', 'Vendedor'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='cliente')
    
    def __str__(self):
        return f"{self.username} ({self.role})"
    
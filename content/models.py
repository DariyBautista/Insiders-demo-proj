from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    FREE = 'free'
    PREMIUM = 'premium'

    ACCESS_CHOICES = [
        (FREE, 'Free'),
        (PREMIUM, 'Premium'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    access_level = models.CharField(
        max_length=10,
        choices=ACCESS_CHOICES,
        default=FREE,
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.access_level})"

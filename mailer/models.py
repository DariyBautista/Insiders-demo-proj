from django.db import models
from django.conf import settings

class EmailSubscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=True)  

    def __str__(self):
        return f"{self.user.username} — {'Підписаний' if self.subscribed else 'Не підписаний'}"

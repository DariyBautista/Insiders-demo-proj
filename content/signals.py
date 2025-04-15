from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post
from subscriptions.models import Subscription
from mailer.models import EmailSubscription
from mailer.utils import send_new_premium_post_email

@receiver(post_save, sender=Post)
def send_premium_post_email(sender, instance, created, **kwargs):
    if created and instance.access_level == Post.PREMIUM:
        active_subs = Subscription.objects.filter(is_active=True)

        for sub in active_subs:
            try:
                email_sub = EmailSubscription.objects.get(user=sub.user)
                if email_sub.subscribed:
                    send_new_premium_post_email(
                        user_email=sub.user.email,
                        user=sub.user,
                        post=instance
                    )
            except EmailSubscription.DoesNotExist:
                continue

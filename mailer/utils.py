from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_html_email(subject, template_name, context, to_email):
    html_content = render_to_string(template_name, context)
    email = EmailMultiAlternatives(
        subject=subject,
        body=html_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[to_email],
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

def send_welcome_email(user_email, user):
    send_html_email(
        subject="👋 Вітаємо у розсилці!",
        template_name="mailer/emails/welcome.html",
        context={'user': user},
        to_email=user_email
    )

def send_payment_success_email(user_email, user, subscription):
    send_html_email(
        subject="✅ Підписка активована!",
        template_name="mailer/emails/paid_success.html",
        context={'user': user, 'subscription': subscription},
        to_email=user_email
    )

def send_new_premium_post_email(user_email, user, post):
    send_html_email(
        subject="🆕 Новий преміум-пост доступний!",
        template_name="mailer/emails/new_premium_post.html",
        context={'user': user, 'post': post},
        to_email=user_email
    )
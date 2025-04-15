from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MailForm
from .utils import send_welcome_email
from .models import EmailSubscription
from django.contrib.auth import get_user_model

User = get_user_model()

def subscribe_view(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']   
            user = request.user if request.user.is_authenticated else None
            if user:
                EmailSubscription.objects.update_or_create(user=user, defaults={'subscribed': True})
            else:
                try:
                    user = User.objects.get(email=email)
                    EmailSubscription.objects.update_or_create(user=user, defaults={'subscribed': True})
                except User.DoesNotExist:
                    messages.error(request, "Цей email не прив'язаний до жодного облікового запису.")
                    return redirect('mailer:subscribe')

            send_welcome_email(email, user=user)
            messages.success(request, "Ви успішно підписались на розсилку!")
            return redirect('mailer:subscribe-success')
    else:
        form = MailForm()
    return render(request, 'mailer/subscribe.html', {'form': form})

def subscribe_success_view(request):
    return render(request, 'mailer/subscribe_success.html')

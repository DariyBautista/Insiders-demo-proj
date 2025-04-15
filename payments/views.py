import stripe #type: ignore
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PaymentForm
from subscriptions.models import Subscription
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from datetime import timedelta
from mailer.utils import send_payment_success_email


@login_required
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
    if request.method == "POST":
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        "price": "price_1RDkqrDAlMiHub2LW1lzoDkN", 
                        'quantity': 1,
                    },
                ],
                mode='subscription',
                success_url="http://127.0.0.1:8000/payments/success/?session_id={CHECKOUT_SESSION_ID}",
                cancel_url=request.build_absolute_uri('/cancel/'),
            )
            return redirect(session.url, code=303)

    return render(request, 'payments/payment.html')

def payment_success(request):
    stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
    session_id = request.GET.get('session_id')
    session = stripe.checkout.Session.retrieve(session_id)

    if session.payment_status == 'paid':
        subscription, created = Subscription.objects.get_or_create(user=request.user)
        subscription.is_active = True
        subscription.plan = 'premium'
        subscription.end_date = timezone.now() + timedelta(days=30)
        subscription.save()

        send_payment_success_email(
            user_email=request.user.email,
            user=request.user,
            subscription=subscription
        )

    return redirect('content:post_list')

def payment_cancel(request):
    return HttpResponse('Оплата була скасована.')
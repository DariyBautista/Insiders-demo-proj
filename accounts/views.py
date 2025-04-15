from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from subscriptions.models import Subscription


@login_required
def dashboard_view(request):
    
    subscription = Subscription.objects.filter(user=request.user, is_active=True).first()

    return render(request, 'accounts/dashboard.html', {'user': request.user, 'subscription': subscription})

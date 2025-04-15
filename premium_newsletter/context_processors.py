from subscriptions.models import Subscription

def active_subscription(request):
    if request.user.is_authenticated:
        subscription = Subscription.objects.filter(user=request.user, is_active=True).first()
        return {'subscription': subscription}
    return {'subscription': None}

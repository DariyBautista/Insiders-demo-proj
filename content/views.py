from django.shortcuts import render, get_object_or_404
from .models import Post
from subscriptions.models import Subscription
from django.contrib.auth.decorators import login_required

@login_required
def post_list(request):
    posts = Post.objects.all()

    if request.user.is_authenticated:
        subscription = Subscription.objects.filter(user=request.user, is_active=True).first()
        if subscription:
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(access_level=Post.FREE)

    return render(request, 'content/post_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'content/post_detail.html', {'post': post})


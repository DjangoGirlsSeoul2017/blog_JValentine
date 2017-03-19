from django.shortcuts import render
from django.utils import timezone

from .models import Post

# Create your views here.
def index(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    simple_posts = Post.objects.order_by('published_date')[:5]

    return render(request, 'blog/index.html', {'simple_posts': simple_posts})

def post_list(request):
    post_list = Post.objects.order_by('published_date')
    return render(request, 'blog/index.html', {'posts': post_list})

def post_view(request):
    posts = Post.objects.order_by('published_date')[:5]
    return render(request, 'blog/index.html', {'posts': posts})
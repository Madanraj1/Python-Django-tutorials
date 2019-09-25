from django.shortcuts import render
from .models import Post
# Create your views here.

def HomePageView(request):
    return render(request, 'posts/index.html')

def PostView(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts.html',{'posts':posts})

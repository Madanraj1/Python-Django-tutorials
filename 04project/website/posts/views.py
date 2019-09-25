from django.shortcuts import render
from posts.models import Post

def HomePageView(request):
    return render(request, 'posts/index.html')

def PostView(request):
    posts = Post.objects.all()
    return render(request, 'posts/post.html',{'posts':posts})

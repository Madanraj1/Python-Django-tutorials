from django.shortcuts import render
from .models import Post


def HomePageView(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html',{'posts':posts})

def ContactView(request):
    return render(request, 'posts/contact_us.html')

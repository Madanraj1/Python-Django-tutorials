from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .models import Post
from posts.forms import CommentForm

class PostListView(ListView):
    model = Post
    template_name = 'posts/homepage.html'


# class PostDetailView(DetailView):
#     form = CommentForm()
#     model = Post
#     context_object_name = 'postt'
#     template_name = 'posts/detail.html'

def PostDetailView(request,id):
    form = CommentForm()
    postt = Post.objects.get(pk=id)
    context = {'postt':postt, 'form':form }
    return render(request, 'posts/detail.html', context)

class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_new.html'
    fields = '__all__'
    # return redirect('home')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    context_object_name = 'postt'
    success_url = reverse_lazy('home')


def CommentView(request, id):
    post = get_object_or_404(Post, pk=id)
    form = CommentForm(request.POST)

    if form.is_valid():
        my_new_todo = Post(commentext=request.POST['text'])
        my_new_todo.save()

    return redirect('post_detail',pk=post.pk)

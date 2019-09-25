from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm

def post_list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'posts/list.html',context)


def post_detail(request, year,day, month,post):
    post = get_object_or_404(Post,
                              slug = post,
                              created__year = year,
                              created__month = month,
                              created__day = day
                             )
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {'post':post, 'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form}
    return render(request, 'posts/detail.html',context)

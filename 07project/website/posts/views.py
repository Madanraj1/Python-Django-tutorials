from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

def Comment_page(request):
	comments = Comment.objects.order_by('-data_added')
	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			new_comment = Comment(comment=request.POST['comments'])
			new_comment.save()
			return redirect('comment_page')
	else:
		form = CommentForm()

	context = {'comments':comments, 'form':form }
	return render(request, 'posts/index.html', context)
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Post, Comment,Profile
from .forms import CommentForm, UserRegistrationForm, CreatePostForm, UserEditForm, ProfileEditForm




@login_required
def edit(request):
    if request.method == 'POST':
        user_form    = UserEditForm(instance=request.user, data=request.POST)

        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, 'Profile updated successfully')
            return redirect('posts_list')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form         = UserEditForm(instance=request.user)
        profile_form      = ProfileEditForm(instance=request.user.profile)

    context = {'user_form':user_form, 'profile_form':profile_form}
    return render(request, 'registration/edit.html', context)



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
                # create a new obj but avoid saving it
                new_user = user_form.save(commit=False)
                #set the field
                new_user.set_password(user_form.cleaned_data['password'])
                # save the user object
                new_user.save()
                Profile.objects.create(user=new_user)
                context = {'new_user':new_user}
                return render(request, 'registration/register_done.html',context)
    else:
        user_form = UserRegistrationForm()

    context = {'user_form':user_form}
    return render(request, 'registration/register.html',context)






@login_required
def post_list(request):
    posts = Post.objects.all()

    post_form = CreatePostForm(request.POST)
    if post_form.is_valid():
        new_post = post_form.save()
        context = {'new_post':new_post}
        return redirect('posts_list')
    else:
        post_form = CreatePostForm()


    context = { 'posts':posts,
                'section':'posts_list',
                'post_form':post_form,
                }
    return render(request,'posts/list.html',context)


def post_detail(request, year,day, month, post):
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

    context = { 'post':post,
                'comments':comments,
                'new_comment':new_comment,
                'comment_form':comment_form
                }
    return render(request, 'posts/detail.html',context)

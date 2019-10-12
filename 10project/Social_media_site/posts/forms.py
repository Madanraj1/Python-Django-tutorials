from django import forms
from .models import Comment,Post
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name','email','body')


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password',widget=forms.PasswordInput)

    password2 = forms.CharField(label='RepeatPassword', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('password don\'t match.' )
        return cd['password2']


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = ('author','title','slug','body')

from django import forms

class CommentForm(forms.Form):
    text = forms.CharField(max_length=50,
    widget=forms.TextInput())

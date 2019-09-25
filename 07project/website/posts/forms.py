from django import forms 

class CommentForm(forms.Form):
	comments = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
		'class':'comment_area',
		'placeholders':'Want to Write something'
		}))
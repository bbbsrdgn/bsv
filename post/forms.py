from django import forms
from .models import Post, Tag, User, Comment
from django.contrib.auth.forms import UserCreationForm
 

class PostForm(forms.ModelForm):
	post = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':90}), label='Soru')
	class Meta: 
		model = Post
		fields = [
			'title',
			'author',
			'post',
			'tags',
			'pub_date',
		]

class TagForm(forms.ModelForm):

	class Meta:
		model = Tag
		fields = [
			'tag',
		]

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = [
			'username',
			'email', 
			'password',
		]

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':100}), label='')
    class Meta:
        model = Comment
        fields = [
        'author', 
        'text',
]


class ContactForm(forms.ModelForm):
	text = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':100}), label='')
	class Meta:
		model = Comment
		fields = [
		'author',
		'text',
		]
		




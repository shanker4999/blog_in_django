from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from blog.models import UserProfile

class CommentForm(forms.Form):
    comment_by_user = forms.CharField(label='Comments',widget=forms.Textarea)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','password','email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture']


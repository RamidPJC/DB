from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *
class NewPost(forms.ModelForm):
    class Meta:
        model = Predlozka
        fields = ('title', 'cont', 'photo', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'cont': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'category': forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}),
        }
        labels = {
            'title': 'Название',
            'cont': 'Содержание',
            'photo': 'Изображение',
            'category': 'Категории'
        }

class Mess(forms.ModelForm):
    class Meta:
        model = Messenger
        fields = ('message',)
        widgets = {
            'message': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic',)
        widgets = {
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'profile_pic': 'Изменить фото',
        }

class AddComment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }

class NewPostAdmin(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'cont', 'photo', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'cont': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'category': forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}),
        }
        labels = {
            'title': 'Название',
            'cont': 'Содержание',
            'photo': 'Изображение',
            'category': 'Категории'
        }

class RatePostForm(forms.ModelForm):
    class Meta:
        model = RatePost
        fields = ('rate',)
        labels = {
            'rate': 'Оценка'
        }
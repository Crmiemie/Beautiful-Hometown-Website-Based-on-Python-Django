from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from core.models import Information, Moment

INPUT_CLASS = 'w-full px-4 py-6 rounded-xl'


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '请输入用户名',
        'class': INPUT_CLASS
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '请输入密码',
        'class': INPUT_CLASS
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '用户名',
        'class': INPUT_CLASS
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': '邮箱地址',
        'class': INPUT_CLASS
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '密码',
        'class': INPUT_CLASS
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '重复密码',
        'class': INPUT_CLASS
    }))




INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ('name', 'gender', 'city')

    name = forms.CharField(label='用户名', widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES
    }))
    gender = forms.CharField(label='性别', widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES
    }))
    city = forms.CharField(label='家乡', widget=forms.TextInput(attrs={
        'placeholder': '填写省份，如：北京',
        'class': INPUT_CLASSES
    }))


class NewMoment(forms.ModelForm):
    class Meta:
        model = Moment
        fields = ('title', 'note', 'image')
        widgets = {
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

    title = forms.CharField(label='标题', widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES
    }))

    note = forms.CharField(label='正文', widget=forms.Textarea(attrs={
        'class': INPUT_CLASSES
    }))
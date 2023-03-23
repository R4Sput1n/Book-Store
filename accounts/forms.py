from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from store.models import Books
from store.models import Authors


class AccountCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AddBookForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        exclude = ['author']
        labels = {
            'pdf_path': 'Upload PDF',
        }


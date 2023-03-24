from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from store.models import Books
from store.models import Series


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

    def __init__(self, profile, *args, **kwargs):
        super(AddBookForm, self).__init__(*args, **kwargs)
        self.fields['series'].queryset = Series.objects.filter(author=profile.author_ref)

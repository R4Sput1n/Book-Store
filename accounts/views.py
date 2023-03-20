from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AccountCreationForm
from accounts.models import OwnedProducts
from store.models import Books
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Congrats, your account with username of {username} has been created!')
            return redirect('store_home')
    else:
        form = AccountCreationForm()

    return render(request, 'store/accounts/register.html', {'form': form})


@login_required
def account(request):
    current_user = request.user
    books_by_user = Books.objects.filter(author=current_user.profile.author_ref)
    owned_books = OwnedProducts.objects.filter(owner_id=current_user.id)
    context = {
        'owned_books': owned_books,
        'books_by': books_by_user,
    }
    return render(request, 'store/accounts/my_account.html', context)


def profile(request, profile):
    profile = User.objects.get(username=profile)
    profile_owned_books = OwnedProducts.objects.filter(owner_id=profile)
    context = {
        'owned_books': profile_owned_books,
        'profile': profile,
    }
    return render(request, 'store/accounts/profile.html', context)


def become_author(request):
    pass
    #some code to send email to admin

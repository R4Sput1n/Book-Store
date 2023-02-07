from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AccountCreationForm
from accounts.models import OwnedProducts


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

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def account(request):
    current_user = request.user
    books = OwnedProducts.objects.filter(owner_id=current_user.id)
    context = {
        'owned_books': books,
    }
    return render(request, 'accounts/my_account.html', context)

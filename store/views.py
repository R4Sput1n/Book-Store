from django.shortcuts import render
from django.db.models import Q
from .models import Books


def home(request):
    context = {
        'books': Books.objects.all(),
        'book_genres': Books.objects.all().order_by('genre').distinct('genre')  # Books are sorted on default
        # by book_title (.models line 35). Distinct needs ordering by itself
    }
    return render(request, 'store/home.html', context)


def genre(request, genre):
    context = {
        'books': Books.objects.filter(genre=genre),
        'book_genres': Books.objects.all().order_by('genre').distinct('genre')  # comment - line 9
    }
    return render(request, 'store/home.html', context)


def search(request):
    searched = request.GET['search']
    context = {
        'books': Books.objects.filter(Q(book_title__icontains=searched) |
                                      Q(genre__icontains=searched) |
                                      Q(author__full_name__icontains=searched)),
        'book_genres': Books.objects.all().order_by('genre').distinct('genre')  # comment - line 9
    }
    if len(context['books']) != 0:
        return render(request, 'store/home.html', context)
    else:
        return render(request, 'store/search_books_fail.html')


def book(request, url_book_name):
    book_name = url_book_name.replace('-', ' ')
    book_id = Books.objects.get(book_title=book_name).book_id
    context = {
        'book': Books.objects.get(pk=book_id)
    }
    return render(request, 'store/book_page.html', context)

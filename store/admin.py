from django.contrib import admin
from .models import Books, Authors, Series


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['book_title', 'author', 'series', 'volume_number', 'genre', 'price']
    list_filter = ['genre']


admin.site.register(Authors)
admin.site.register(Series)

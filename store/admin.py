from django.contrib import admin
from .models import Books, Authors, Series

admin.site.register(Books)
admin.site.register(Authors)
admin.site.register(Series)
from django.db import models
from django.contrib.auth.models import User
from store.models import Books
from store.models import Authors


class UserAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_author = models.BooleanField(default=False)
    author_ref = models.ForeignKey(Authors, on_delete=models.DO_NOTHING, blank=True, null=True)


class OwnedProducts(models.Model):
    owner = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(Books, models.DO_NOTHING, blank=True, null=True)


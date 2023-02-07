from django.db import models
from django.contrib.auth.models import User
from store.models import Books

# Create your models here.

#
# class Accounts(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     account_id = models.UUIDField(primary_key=True)
#     login = models.CharField(max_length=50)
#     email = models.CharField(max_length=100)
#     salt = models.UUIDField()
#     passhash = models.TextField()
#
#     def __str__(self):
#         return self.login
#
#     class Meta:
#         managed = False
#         db_table = 'accounts'
#         unique_together = (('login', 'email'),)


class OwnedProducts(models.Model):
    owner = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(Books, models.DO_NOTHING, blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'owned_products'


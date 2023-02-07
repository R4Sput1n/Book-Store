from django.db import models
from django.contrib.auth.models import User
from store.models import Books


class Cart(models.Model):
    order_id = models.SmallAutoField(primary_key=True)
    customer = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(Books, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f'{self.order_id}, {self.customer.username}, {self.product.book_title}'

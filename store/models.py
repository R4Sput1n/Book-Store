from django.db import models


class Authors(models.Model):
    author_id = models.SmallAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # class Meta:
    #     managed = False
    #     db_table = 'authors'


class Series(models.Model):
    series_id = models.SmallAutoField(primary_key=True)
    series_name = models.CharField(max_length=50)
    volume_count = models.SmallIntegerField()
    author = models.ForeignKey(Authors, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.series_name
    #
    # class Meta:
    #     managed = False
    #     db_table = 'series'


class Books(models.Model):
    book_id = models.SmallAutoField(primary_key=True)
    book_title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Authors, models.DO_NOTHING, blank=True, null=True)
    series = models.ForeignKey(Series, models.DO_NOTHING, blank=True, null=True)
    volume_number = models.SmallIntegerField()
    cover = models.ImageField(default='default.jpg', upload_to='covers')
    pdf_path = models.FileField(default='default.pdf', upload_to='pdfs')
    genre = models.CharField(max_length=25, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=9.99)

    def __str__(self):
        return self.book_title

    # class Meta:
    #     managed = False
    #     db_table = 'books'


# class Edition(models.Model):
#     product_id = models.SmallAutoField(primary_key=True)
#     book = models.ForeignKey(Books, models.DO_NOTHING, blank=True, null=True)
#     publisher = models.ForeignKey('Publisher', models.DO_NOTHING, blank=True, null=True)
#     lang = models.CharField(max_length=50)
#     price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'edition'
#
#
# class Publisher(models.Model):
#     publisher_id = models.SmallAutoField(primary_key=True)
#     publishing_house = models.CharField(max_length=50)
#     country = models.CharField(max_length=25, blank=True, null=True)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'publisher'
#


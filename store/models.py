from django.db import models


class Authors(models.Model):
    author_id = models.SmallAutoField(primary_key=True)
    full_name = models.CharField(max_length=100, default='DELETE THIS')

    def __str__(self):
        return self.full_name


class Series(models.Model):
    series_id = models.SmallAutoField(primary_key=True)
    series_name = models.CharField(max_length=50)
    volume_count = models.SmallIntegerField()
    author = models.ForeignKey(Authors, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.series_name


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

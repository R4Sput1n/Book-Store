# Generated by Django 4.1.4 on 2023-02-01 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_books_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='pdf_path',
            field=models.FileField(default='default.pdf', upload_to='pdfs'),
        ),
    ]

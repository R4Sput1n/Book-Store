# Generated by Django 4.1.4 on 2023-01-04 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_books_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='cover',
            field=models.ImageField(default='media/covers/default.jpg', upload_to='covers'),
        ),
    ]

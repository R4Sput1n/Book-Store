# Generated by Django 4.1.4 on 2023-02-15 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_books_pdf_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authors',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='authors',
            name='last_name',
        ),
        migrations.AddField(
            model_name='authors',
            name='full_name',
            field=models.CharField(default='DELETE THIS', max_length=100),
        ),
    ]

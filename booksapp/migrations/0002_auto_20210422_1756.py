# Generated by Django 3.1.7 on 2021-04-22 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='date',
            new_name='published_date',
        ),
    ]

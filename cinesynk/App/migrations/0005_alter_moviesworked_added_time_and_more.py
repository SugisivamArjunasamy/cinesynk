# Generated by Django 4.2.11 on 2024-03-10 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_remove_professionaluser_movies_worked_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesworked',
            name='added_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='posted_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
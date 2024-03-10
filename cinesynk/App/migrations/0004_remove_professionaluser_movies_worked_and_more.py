# Generated by Django 4.2.11 on 2024-03-10 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_professionaluser_posts_professionaluser_profile_img_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professionaluser',
            name='movies_worked',
        ),
        migrations.RemoveField(
            model_name='professionaluser',
            name='posts',
        ),
        migrations.AlterField(
            model_name='professionaluser',
            name='user_type',
            field=models.TextField(default='', max_length=512),
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.TextField(default='', max_length=512)),
                ('post_type', models.TextField(default='', max_length=512)),
                ('description', models.TextField(default='', max_length=512)),
                ('posted_time', models.DateTimeField()),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.professionaluser')),
            ],
        ),
        migrations.CreateModel(
            name='MoviesWorked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.TextField(default='', max_length=512)),
                ('title', models.CharField(default='', max_length=125)),
                ('description', models.TextField(default='', max_length=512)),
                ('added_time', models.DateTimeField()),
                ('worked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.professionaluser')),
            ],
        ),
    ]
# Generated by Django 4.0.2 on 2022-02-22 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0010_alter_movie_slug_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
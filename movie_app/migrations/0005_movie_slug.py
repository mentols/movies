# Generated by Django 4.0.2 on 2022-02-21 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_movie_budget_movie_year_alter_movie_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
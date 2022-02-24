from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Man'),
        (FEMALE, 'Women'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def __str__(self):
        if self.sex == self.MALE:
            return f'Actor {self.first_name} {self.last_name}'
        else:
            return f'Actriss {self.first_name} {self.last_name}'



class Movie(models.Model):
    EUR = 'EUR'
    RUB = 'RUB'
    USD = 'USD'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Rubles')
    ]

    name = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    year = models.IntegerField(null=True)
    budget = models.IntegerField(null=True, blank=True,
                                 validators=[MinValueValidator(0), MaxValueValidator(10000000000)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=USD)
    slug = models.SlugField(default='', null=False)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True, related_name='movies')
    actors = models.ManyToManyField(Actor)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie_detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}. Year: {self.year} with budget {self.budget}'

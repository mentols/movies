from django.contrib import admin, messages
from django.db.models import QuerySet

from .models import Movie, Director, Actor

admin.site.register(Director)
admin.site.register(Actor)


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('меньше 40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 85', 'Высокий'),
            ('больше 85', 'Наивысший'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == 'меньше 40':
            return queryset.filter(rating__lt=40)
        elif self.value() == 'от 40 до 59':
            return queryset.filter(rating__gt=40).filter(rating__lt=59)
        elif self.value() == 'от 60 до 85':
            return queryset.filter(rating__gt=60).filter(rating__lt=85)
        elif self.value() == 'больше 85':
            return queryset.filter(rating__gt=86)


# admin.site.register(Movie, MovieAdmin)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # filter_horizontal = ['actors']
    filter_vertical = ['actors']
    # fields = ['name', 'rating']
    # exclude = ['slug']
    list_display = ['name', 'rating', 'year', 'director', 'currency', 'rating_status']
    list_editable = ['rating', 'year', 'director', 'currency']
    # ordering = ['rating']
    list_per_page = 5
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name']
    list_filter = ['currency', RatingFilter]

    # RatingFilter
    @admin.display(ordering='rating', description='RATING STATUS')
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return 'Не интересный фильм'
        elif movie.rating < 70:
            return 'Обычный фильм'
        elif movie.rating <= 85:
            return 'Хороший фильм'
        return 'Наилучший выбор'

    @admin.action(description='Вся валюта в доллары')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Вся валюта в евро')
    def set_euro(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EUR)
        self.message_user(request, f"Было обновлено {count_updated} элемента в евро", messages.WARNING)

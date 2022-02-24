from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_all_movie, name='start'),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie_detail'),
    path('directors/', views.show_all_directors, name='all_dirs'),
    path('directors/<str:one_director>', views.show_director, name='director')
]

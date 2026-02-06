from django.urls import path
from . import views

urlpatterns = [
    # HTML pages
    path('', views.item_list, name='item_list'),
    path('items/<int:pk>/', views.item_detail, name='item_detail'),

    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),

    # API endpoints
    path('api/movies/', views.movie_list_api, name='movie_list_api'),
    path('api/movies/<int:pk>/', views.movie_detail_api, name='movie_detail_api'),
]

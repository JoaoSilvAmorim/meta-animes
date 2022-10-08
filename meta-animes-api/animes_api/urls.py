from django.urls import path

from animes_api import views

urlpatterns = [ 
    path('register_chapter/', views.chapters.as_view()),
    path('register_anime/', views.animes.as_view()),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.word_list, name='list'),
    path('add/', views.add_word, name='add'),
    path('edit/<int:pk>/', views.edit_word, name='edit'),
    path('quiz/', views.quiz, name='quiz'),
]
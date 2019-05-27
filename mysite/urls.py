from django.contrib import admin
from django.urls import path
from mysite import views

app_name = 'mysite'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('<int:secretcode_id>/select', views.select, name='select'),
    path('<int:secretcode_id>/mission_map', views.mission_map, name='mission_map'),
    path('<int:secretcode_id>/mission_quiz', views.mission_quiz, name='mission_quiz'),
    path('api_quiz', views.api_quiz, name='api_quiz'),
    path('<int:secretcode_id>/api_save_mission', views.api_save_mission, name='api_save_mission'),
    path('<int:secretcode_id>/api_save_quizs', views.api_save_quizs, name='api_save_quizs'),
    path('<int:secretcode_id>/api_save_words', views.api_save_words, name='api_save_words'),
    path('<int:secretcode_id>/api_save_mission_map', views.api_save_mission_map, name='api_save_mission_map'),
    path('<int:secretcode_id>/api_reset_mission_map', views.api_reset_mission_map, name='api_reset_mission_map'),
    path('map_test', views.map_test, name='map_test'),
]
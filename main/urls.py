from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from quizengine import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('quiz/', views.quiz, name="quiz"),
    path('thanks/', views.thanks, name="thanks")
]
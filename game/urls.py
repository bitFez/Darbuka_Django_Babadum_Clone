from django.urls import path

from . import views

app_name = 'game'

urlpatterns = [
    path('add_words', views.add_words, name="addwords"),
    path('play/us', views.play_us, name="play_us"),
]

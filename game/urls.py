from django.urls import path, re_path

from . import views

app_name = 'game'

urlpatterns = [
    path('add_words', views.add_words, name="addwords"),
    path('play/us', views.play_us, name="play_us"),
    path('play/uk', views.play_uk, name="play_uk"),
    path('play/tr', views.play_tr, name="play_tr"),
    path('play/ar', views.play_ar, name="play_ar"),
    path('play/ur', views.play_ur, name="play_ur"),
    path('play/az', views.play_az, name="play_az"),
    #re_path(r'^play/check/(?P<word1>\w+)/(?P<clue>\w+)/$', views.check_answer, name="checka"),
    path('play/check', views.check_answer, name="checka"),
    path('highscores', views.high_scores, name="high_scores"),
    path('stats', views.word_stats, name="word_stats"),
    
]

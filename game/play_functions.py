from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from random import shuffle

from .models import League, Word, LanguageScore
from profiles.models import UserProfile

import arabic_reshaper
from bidi.algorithm import get_display

@login_required(login_url='/accounts/login/')
def play_us(request):
    user = UserProfile.objects.get(id=request.user.id)
    language = League.objects.get(id=1)
    if LanguageScore.objects.filter(user=request.user, language=language.id).exists():
        user_lan = LanguageScore.objects.get(user=request.user, language=language.id)
    else:
        user_lan = LanguageScore.objects.get_or_create(
            user = request.user,
            language = language,
            points = 0
        )
        user_lan = LanguageScore.objects.get(user=request.user, language=language.id)
    user_lan_points = user_lan.points 
    id = League.objects.get(id=1)
    word = Word.objects.all().filter(language=id).order_by('?')
    rndw1,rndw2,rndw3,rndw4 = word[0],word[1],word[2],word[3]
    correct_word = rndw1
    words_list = [rndw1,rndw2,rndw3,rndw4]
    shuffle(words_list)

    context ={
        "word1":words_list[0],
        "word2":words_list[1],
        "word3":words_list[2],
        "word4":words_list[3],
        "clue":correct_word,
        "flag":"/media/images/us.svg",
        "lan_score":user_lan_points,
        "language":language,
        "glo_score":user.points,
        "correct_word_img":word[0].image
    }
    
    return render(request, 'game/game_template.html', context)

@login_required(login_url='/accounts/login/')
def play_uk(request):
    user = UserProfile.objects.get(id=request.user.id)
    language = League.objects.get(id=2)
    if LanguageScore.objects.filter(user=request.user, language=language.id).exists():
        user_lan = LanguageScore.objects.get(user=request.user, language=language.id)
    else:
        user_lan = LanguageScore.objects.get_or_create(
            user = request.user,
            language = language,
            points = 0
        )
        user_lan = LanguageScore.objects.get(user=request.user, language=language.id)
    user_lan_points = user_lan.points 
    word = Word.objects.all().filter(language=language.id).order_by('?')
    rndw1,rndw2,rndw3,rndw4 = word[0],word[1],word[2],word[3]
    correct_word = rndw1
    words_list = [rndw1,rndw2,rndw3,rndw4]
    shuffle(words_list)

    context ={
        "word1":words_list[0],
        "word2":words_list[1],
        "word3":words_list[2],
        "word4":words_list[3],
        "clue":correct_word,
        "flag":"/media/images/uk.svg",
        "lan_score":user_lan_points,
        "language":language,
        "glo_score":user.points,
        "correct_word_img":word[0].image
    }
    
    return render(request, 'game/game_template.html', context)

@login_required(login_url='/accounts/login/')
def play_tr(request):
    user = UserProfile.objects.get(id=request.user.id)
    language = League.objects.get(id=3)
    if LanguageScore.objects.filter(user=request.user, language=language.id).exists():
        user_lan = LanguageScore.objects.get(user=request.user, language=language.id)
    else:
        user_lan = LanguageScore.objects.get_or_create(
            user = request.user,
            language = language,
            points = 0
        )
        user_lan = LanguageScore.objects.get(user=request.user, language=language.id)
    user_lan_points = user_lan.points
    id = League.objects.get(id=3)
    word = Word.objects.all().filter(language=id).order_by('?')
    rndw1,rndw2,rndw3,rndw4 = word[0],word[1],word[2],word[3]
    correct_word = rndw1
    words_list = [rndw1,rndw2,rndw3,rndw4]
    shuffle(words_list)

    context ={
        "word1":words_list[0],
        "word2":words_list[1],
        "word3":words_list[2],
        "word4":words_list[3],
        "clue":correct_word,
        "flag":"/media/images/tr.svg",
        "lan_score":user_lan_points, 
        "language":language,
        "glo_score":user.points,
        "correct_word_img":word[0].image
    }
    
    return render(request, 'game/game_template.html', context)

@login_required(login_url='/accounts/login/')
def play_ar(request):
    user = UserProfile.objects.get(id=request.user.id)
    language = League.objects.get(id=4)
    if LanguageScore.objects.filter(user=request.user, language=language.id).exists():
        user_lan = LanguageScore.objects.get(user=request.user, language=language.id)
    else:
        user_lan = LanguageScore.objects.get_or_create(
            user = request.user,
            language = language,
            points = 0
        )
        user_lan = LanguageScore.objects.get(user=request.user, language=language.id)
    user_lan_points = user_lan.points
    id = League.objects.get(id=4)
    word = Word.objects.all().filter(language=id).order_by('?')
    rndw1,rndw2,rndw3,rndw4 = word[0],word[1],word[2],word[3]
    correct_word = rndw1
    words_list = [rndw1,rndw2,rndw3,rndw4]
    shuffle(words_list)

    context ={
        "word1":words_list[0],
        "word2":words_list[1],
        "word3":words_list[2],
        "word4":words_list[3],
        "clue":correct_word,
        "flag":"/media/images/palestine.svg",
        "lan_score":user_lan_points, 
        "language":language,
        "glo_score":user.points,
        "correct_word_img":word[0].image
    }
    
    return render(request, 'game/game_template.html', context)

@login_required(login_url='/accounts/login/')
def play_az(request):
    user = UserProfile.objects.get(id=request.user.id)
    language = League.objects.get(id=5)
    if LanguageScore.objects.filter(user=request.user, language=language.id).exists():
        user_lan = LanguageScore.objects.get(user=request.user, language=language.id)
    else:
        user_lan = LanguageScore.objects.get_or_create(
            user = request.user,
            language = language,
            points = 0
        )
        user_lan = LanguageScore.objects.get(user=request.user, language=language.id)
    user_lan_points = user_lan.points
    id = League.objects.get(id=5)
    word = Word.objects.all().filter(language=id).order_by('?')
    rndw1,rndw2,rndw3,rndw4 = word[0],word[1],word[2],word[3]
    correct_word = rndw1
    words_list = [rndw1,rndw2,rndw3,rndw4]
    shuffle(words_list)

    context ={
        "word1":words_list[0],
        "word2":words_list[1],
        "word3":words_list[2],
        "word4":words_list[3],
        "clue":correct_word,
        "flag":"/media/images/az.svg",
        "lan_score":user_lan_points, 
        "language":language,
        "glo_score":user.points, 
        "correct_word_img":word[0].image
    }
    
    return render(request, 'game/game_template.html', context)

@login_required(login_url='/accounts/login/')
def play_ur(request):
    user = UserProfile.objects.get(id=request.user.id)
    language = League.objects.get(id=6)
    if LanguageScore.objects.filter(user=request.user, language=language.id).exists():
        user_lan = LanguageScore.objects.get(user=request.user, language=language.id)
    else:
        user_lan = LanguageScore.objects.get_or_create(
            user = request.user,
            language = language,
            points = 0
        )
        user_lan = LanguageScore.objects.get(user=request.user, language=language.id)
    user_lan_points = user_lan.points
    id = League.objects.get(id=6)
    word = Word.objects.all().filter(language=id).order_by('?')
    rndw1,rndw2,rndw3,rndw4 = word[0],word[1],word[2],word[3]
    correct_word = rndw1
    words_list = [rndw1,rndw2,rndw3,rndw4]
    shuffle(words_list)

    context ={
        "word1":words_list[0],
        "word2":words_list[1],
        "word3":words_list[2],
        "word4":words_list[3],
        "clue":correct_word,
        "flag":"/media/images/pk.svg",
        "lan_score":user_lan_points, 
        "language":language,
        "glo_score":user.points,
        "correct_word_img":word[0].image
    }
    
    return render(request, 'game/game_template.html', context)

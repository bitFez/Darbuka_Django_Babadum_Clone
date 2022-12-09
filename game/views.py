from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_htmx.http import trigger_client_event
from random import shuffle
import json

from .models import League, Word, LanguageScore
from profiles.models import UserProfile

import arabic_reshaper
from bidi.algorithm import get_display
ar_configuration = {
    'delete_harakat': False,
    'support_ligatures': True,
    'RIAL SIGN': True,  # Replace ر ي ا ل with ﷼
}
reshaper = arabic_reshaper.ArabicReshaper(configuration=ar_configuration)

# Create your views here.
def add_words(request):
    # Opening JSON file
    with open(r'game\file_dict.json', encoding="utf8") as f:
        data = json.load(f)
    
    lenofdata = len(data)
    for i in range(0, len(data)):
        perc = round((i / lenofdata) * 100,2)
        ide = League.objects.get(id=1)
        print(f' ... {perc}%') # {data[i]["us"]} ... len is {len(data[i]["us"])}
        obj = Word.objects.update_or_create(
            language = ide,
            word = data[i]['us'],
            code = data[i]["code"],
            image = data[i]["filename"]
        )
        ide = League.objects.get(id=2)
        if len(data[i]['uk']) > 0:
            obj = Word.objects.update_or_create(
                language = ide,
                word = data[i]['uk'],
                code = data[i]["code"],
                image = data[i]["filename"]
            )
        else:
            obj = Word.objects.update_or_create(
                language = ide,
                word = data[i]['us'],
                code = data[i]["code"],
                image = data[i]["filename"]
            )
        ide = League.objects.get(id=3)
        if len(data[i]['tr']) > 0:
            obj = Word.objects.update_or_create(
                language = ide,
                word = data[i]['tr'],
                code = data[i]["code"],
                image = data[i]["filename"]
            )
        ide = League.objects.get(id=4)
        if len(data[i]['ar']) > 0:
            tbr = reshaper.reshape(data[i]['ar'])
            result = get_display(tbr)
            obj = Word.objects.update_or_create(
                language = ide,
                word = result,
                code = data[i]["code"],
                image = data[i]["filename"]
            )

@login_required(login_url='/accounts/login/')
def play_us(request):
    user = UserProfile.objects.get(id=request.user.id)
    if LanguageScore.objects.filter(user=request.user).exists():
        user_lan = LanguageScore.objects.get(user=request.user)
    else:
        user_lan = LanguageScore.objects.get_or_create(
            user = request.user,
            language = League.objects.get(id=1)
        )
    user_lan_points = user_lan.points
    if request.method == "POST":
        # if not instance.likes.filter(id=request.user.id).exists():
        #     instance.likes.add(request.user)
        #     instance.save() 
        #     return render( request, 'posts/partials/likes_area.html', context={'post':instance})
        pass
    else:    
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
        "flag":"https://flagcdn.com/40x30/us.png",
        "lan_score":user_lan_points,
        "language":user_lan.id,
        "glo_score":user.points
    }
    
    return render(request, 'game/game_template.html', context)

@login_required(login_url='/accounts/login/')
def play_tr(request):
    user = UserProfile.objects.get(id=request.user.id)
    if LanguageScore.objects.filter(user=request.user, language=3).exists():
        user_lan = LanguageScore.objects.get(user=request.user,language=3)
    else:
        user_lan = LanguageScore.objects.get_or_create(
            user = request.user,
            language = League.objects.get(id=3),
            points = 0
        )
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
        "flag":"https://flagcdn.com/40x30/tr.png",
        "lan_score":user_lan_points, 
        "language":user_lan.id,
        "glo_score":user.points
    }
    
    return render(request, 'game/game_template.html', context)

@login_required(login_url='/accounts/login/')
def play_ar(request):
    user = UserProfile.objects.get(id=request.user.id)
    if LanguageScore.objects.filter(user=request.user, language=4).exists():
        user_lan = LanguageScore.objects.get(user=request.user, language=4)
    else:
        user_lan = LanguageScore.objects.get_or_create(
            user = request.user,
            language = League.objects.get(id=4),
            points = 0
        )
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
        "flag":"https://flagcdn.com/40x30/sa.png",
        "lan_score":user_lan_points, 
        "language":user_lan.id,
        "glo_score":user.points
    }
    
    return render(request, 'game/game_template.html', context)

def check_answer(request):
    
    if request.method == "POST":
        # loads hidden fields from answer submissions
        word = request.POST["word"]
        clue = request.POST["clue"]
        lang = request.POST["language"]
        flag = request.POST["flag"]
        
        # pulling up user score for language being tested 
        user = request.user
        lan = LanguageScore.objects.get(id=lang)
        
        # checks submitted answer against correct answer
        # and updates score based on correctness
        a = Word.objects.all().filter(word=word).first()
        b = Word.objects.all().filter(word=clue).first()
        # print(f"Word {a.word}, answer {b.word}")
        if a.word == b.word:
            print("Answer was correct")
            user.points += 1
            user.save()
            lan.points += 1
            lan.save()
            context = {
                "lan_score":lan.points,
                "glo_score":user.points,
                "flag":flag,
            }
            response = render(request, 'game/partials/scoreboard.html', context)
            return trigger_client_event(
                response, 
                'open-btn', context
            )
        else:
            print("Answer not correct")
            user.points -= 1
            user.save()
            lan.points -= 1
            lan.save()
            context = {
                "lan_score":lan.points,
                "glo_score":user.points,
                "flag":flag,
            }
            # loads partial section on page for the score
            # return render(request, 'game/partials/scoreboard.html', context)
            response = render(request, 'game/partials/scoreboard.html', context)
            return trigger_client_event(
                response, 
                'popup_window', context
            ) 
        
    else:
        print("Not post request")
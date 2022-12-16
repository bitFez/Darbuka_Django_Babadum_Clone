from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_htmx.http import trigger_client_event
from random import shuffle
import json
from . play_functions import *
from .models import League, Word, LanguageScore
from profiles.models import UserProfile
from django.db.models import Sum
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
    # r'game\file_dict.json'
    with open(r'c:\Coding\Django_Babadum_Clone\game\file_dict.json', encoding="utf8") as f:
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
        ide = League.objects.get(id=5)
        if len(data[i]['az']) > 0:
            obj = Word.objects.update_or_create(
                language = ide,
                word = data[i]['az'],
                code = data[i]["code"],
                image = data[i]["filename"]
            )
        ide = League.objects.get(id=6)
        if len(data[i]['ur']) > 0:
            tbr = reshaper.reshape(data[i]['ur'])
            result = get_display(tbr)
            obj = Word.objects.update_or_create(
                language = ide,
                word = result,
                code = data[i]["code"],
                image = data[i]["filename"]
            )


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
        a = Word.objects.all().filter(word=word, language=lang).first()
        b = Word.objects.all().filter(word=clue, language=lang).first()
        b.frequency += 1
        # print(f"Word {a.word}, answer {b.word}")
        if a.word == b.word:
            print("Answer was correct")
            user.points += 1
            user.save()
            lan.points += 1
            lan.save()
            b.correctAnswerCount += 1
            b.save()
            context = {
                "lan_score":lan.points,
                "glo_score":user.points,
                "flag":flag,

            }
            response = render(request, 'game/partials/scoreboard.html', context)
            return trigger_client_event(
                response, 
                'correct-answer', context
            )
        else:
            print("Answer not correct")
            user.points -= 1
            user.save()
            lan.points -= 1
            lan.save()
            b.incorrectAnswerCount += 1
            b.save()
            context = {
                "lan_score":lan.points,
                "glo_score":user.points,
                "flag":flag                
            }
            # loads partial section on page for the score
            # return render(request, 'game/partials/scoreboard.html', context)
            response = render(request, 'game/partials/scoreboard.html', context)
            return trigger_client_event(
                response, 
                'incorrect-answer', context
            ) 
        
    else:
        print("Not post request")

def high_scores(request):
    users = UserProfile.objects.all()

    languages = LanguageScore.objects.all()
    context = {"langs":languages, "users":users}
    return render(request, 'game/high-scores.html', context)

def word_stats(request):
    correct = Word.objects.aggregate(total = Sum('correctAnswerCount'))
    incorrect = Word.objects.aggregate(total = Sum('incorrectAnswerCount'))
    frequency = Word.objects.aggregate(total = Sum('frequency'))
    corr_per = round(correct["total"] / frequency["total"] *100,2)
    usEnglish = Word.objects.filter(language=1).aggregate(total= Sum('correctAnswerCount'))
    usEnglishfre = Word.objects.filter(language=1).aggregate(total= Sum('frequency'))
    usEngCorr = round(usEnglish["total"] / usEnglishfre["total"] *100,1)

    ukEnglish = Word.objects.filter(language=2).aggregate(total= Sum('correctAnswerCount'))
    ukEnglishfre = Word.objects.filter(language=2).aggregate(total= Sum('frequency'))
    ukEngCorr = round(ukEnglish["total"] / ukEnglishfre["total"] *100,1)

    tr = Word.objects.filter(language=3).aggregate(total= Sum('correctAnswerCount'))
    trfre = Word.objects.filter(language=3).aggregate(total= Sum('frequency'))
    trCorr = round(tr["total"] / trfre["total"] *100,1)

    context = {
        "correct":correct, "corr_per":corr_per, "incorrect":incorrect,
        "usEnglishAns":usEnglishfre, "usEngPer":usEngCorr, 
        "ukEnglishAns":ukEnglishfre, "ukEngPer":ukEngCorr,
        "trAns":trfre, "trCorr":trCorr,
        
                }
    return render(request, 'game/stats.html', context)
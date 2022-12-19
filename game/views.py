from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_htmx.http import trigger_client_event
from random import shuffle
import json
from django.core.paginator import Paginator

from . play_functions import *
from .models import League, Word, LanguageScore
from profiles.models import UserProfile
from django.db.models import Sum, Count, F, FloatField, ExpressionWrapper
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
    # r'c:\Coding\Django_Babadum_Clone\game\file_dict.json'
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
        language_id = League.objects.all().filter(language=lang).first()
        lan = LanguageScore.objects.all().filter(language=language_id.id, user=user).first()
        # checks submitted answer against correct answer
        # and updates score based on correctness
        a = Word.objects.all().filter(word=word, language=language_id).first()
        b = Word.objects.all().filter(word=clue, language=language_id).first()
        b.frequency += 1
        # print(f"Word {a.word}, answer {b.word}")
        if a.word == b.word:
            #print("Answer was correct")
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
            #print("Answer not correct")
            if user.points > 0:
                user.points -= 1
                user.save()
            if lan.points >0:
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
    paginator = Paginator(users, 10)
    
    page_number = request.GET.get('page')
    user_scores = paginator.get_page(page_number)

    languages = LanguageScore.objects.all()
    context = {"langs":languages, "users":users, "user_scores":user_scores}

    if request.htmx:
        return render(request, "posts/partials/top10users.html", context)
    else:
        return render(request, 'game/high-scores.html', context)
    


def get_average_correct(correct_count, frequency):
    if frequency == 0:
        return 0
    else:
        return round(correct_count / frequency *100,2)

def word_stats(request):
    stats = []
    correct = Word.objects.aggregate(total = Sum('correctAnswerCount'))
    incorrect = Word.objects.aggregate(total = Sum('incorrectAnswerCount'))
    frequency = Word.objects.aggregate(total = Sum('frequency'))
    corr_per = get_average_correct(correct["total"],frequency["total"])
    inCorr_perc = get_average_correct(incorrect["total"],frequency["total"])
    usEnglish = Word.objects.filter(language=1).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    usEngCorr = round(usEnglish["total"] / usEnglish["frequency"] *100,1)

    ukEnglish = Word.objects.filter(language=2).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    ukEngCorr = round(get_average_correct(ukEnglish["total"], ukEnglish["frequency"]),2)

    tr = Word.objects.filter(language=3).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    trCorr = round(get_average_correct(tr["total"],tr["frequency"]),2)

    ar = Word.objects.filter(language=4).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    arCorr = round(get_average_correct(ar["total"], ar["frequency"]),2)

    az = Word.objects.filter(language=5).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    azCorr = round(get_average_correct(az["total"], az["frequency"]),)

    ur = Word.objects.filter(language=6).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    urCorr = round(get_average_correct(ur["total"],ur["frequency"]),)

    
    all_words_easiest = Word.objects.filter(frequency__gt=0).order_by("-correctAnswerCount").annotate(perc=Sum(F("correctAnswerCount")/F("frequency")*100))[:10]

    
    all_words_hardest = Word.objects.filter(frequency__gt=0).annotate(perc=Sum(F("correctAnswerCount")/F("frequency")*100)).order_by("perc", )[:10]
    
    
    data = {
        0:{"language":"Azeri","attempts":az["frequency"], "correctAnswers":azCorr},
        1:{"language":"US English","attempts":usEnglish["frequency"], "correctAnswers":usEngCorr},
        2:{"language":"UK English","attempts":ukEnglish["frequency"], "correctAnswers":ukEngCorr},
        3:{"language":"Turkish","attempts":tr["frequency"], "correctAnswers":trCorr},
        4:{"language":"Arabic","attempts":ar["frequency"], "correctAnswers":arCorr},
        5:{"language":"Urdu","attempts":ur["frequency"], "correctAnswers":urCorr}
    }
    res = sorted(data, key=lambda x: (data[x]['attempts']), reverse=True)
    
    stats = {}
    
    for r in range(0,len(res)):
        dict1 = {r:{
            "language":data[res[r]]["language"],
            "attempts":data[res[r]]["attempts"],
            "correctAnswers":data[res[r]]["correctAnswers"],
            "perOfTotalQs":((data[res[r]]["attempts"]/frequency['total'])*100),
            }}
        stats.update(dict1)

    context = {
        "correct":correct, "inCorr_perc":inCorr_perc,"corr_per":corr_per, "incorrect":incorrect,
        "stats":stats, "awe":all_words_easiest,"awh":all_words_hardest,
                }
    return render(request, 'game/stats.html', context)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_htmx.http import trigger_client_event
from django.http import HttpResponse
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
    
    #
    # variables to count number of new languages and words added
    newWords = 0
    newLanguages = 0

    # 
    # make sure that the leagues exists before adding words.
    leagues = {
        0:{"language":"English (American)", "name":"us", "questionCount":0},
        1:{"language":"English (British)", "name":"uk", "questionCount":0},
        2:{"language":"Turkish", "name":"tr", "questionCount":0},
        3:{"language":"Arabic", "name":"ar", "questionCount":0},
        4:{"language":"Azeri", "name":"az", "questionCount":0},
        5:{"language":"Urdu", "name":"ur", "questionCount":0},
        6:{"language":"Ottoman Turkish", "name":"ot", "questionCount":0},
        7:{"language":"Cypriot Turkish", "name":"kt", "questionCount":0},
        8:{"language":"Kazakh", "name":"kk", "questionCount":0},
        9:{"language":"Turkmen", "name":"tk", "questionCount":0},
        10:{"language":"Tatar", "name":"tt", "questionCount":0},
        11:{"language":"Kirghiz", "name":"ky", "questionCount":0},
        12:{"language":"Uzbek", "name":"uz", "questionCount":0},
        13:{"language":"Uyghur", "name":"ug", "questionCount":0},
    }
    # for lan in range(0, len(leagues)):
    #     print(f"{leagues[lan]['name']}")
    for lan in range(0, len(leagues)):
        lang = leagues[lan]["name"]
        nam = leagues[lan]["language"]
        que = leagues[lan]["questionCount"]
        if not League.objects.filter(name=nam).exists():
            obj = League.objects.update_or_create(
                language = lang,
                name = nam,
                questionCount = que,
            )
            newLanguages += 1
            print(f"added language {lang}")
        else:
            print(f"{lang} already exists")
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
        newWords += 1
        ide = League.objects.get(id=2)
        if len(data[i]['uk']) > 0:
            obj = Word.objects.update_or_create(
                language = ide,
                word = data[i]['uk'],
                code = data[i]["code"],
                image = data[i]["filename"]
            )
            newWords += 1
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
            newWords += 1
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
            newWords += 1
        ide = League.objects.get(id=5)
        if len(data[i]['az']) > 0:
            obj = Word.objects.update_or_create(
                language = ide,
                word = data[i]['az'],
                code = data[i]["code"],
                image = data[i]["filename"]
            )
            newWords += 1
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
            newWords += 1
        ide = League.objects.get(id=7)
        if len(data[i]['ot']) > 0:
            tbr = reshaper.reshape(data[i]['ot'])
            result = get_display(tbr)
            obj = Word.objects.update_or_create(
                language = ide,
                word = result,
                code = data[i]["code"],
                image = data[i]["filename"]
            )
            newWords += 1
        ide = League.objects.get(id=8)
        if len(data[i]['kt']) > 0:
            obj = Word.objects.update_or_create(
                language = ide,
                word = data[i]['kt'],
                code = data[i]["code"],
                image = data[i]["filename"]
            )
            newWords += 1
        else:
            obj = Word.objects.update_or_create(
                language = ide,
                word = data[i]['tr'],
                code = data[i]["code"],
                image = data[i]["filename"]
            )
        ide = League.objects.get(id=9)
        if len(data[i]['kk']) > 0:
            obj = Word.objects.update_or_create(
                language = ide,
                word = data[i]['kk'],
                code = data[i]["code"],
                image = data[i]["filename"]
            )
            newWords += 1
        ide = League.objects.get(id=10)
        if len(data[i]['tk']) > 0:
            obj = Word.objects.update_or_create(
                language = ide,
                word = data[i]['tk'],
                code = data[i]["code"],
                image = data[i]["filename"]
            )
            newWords += 1
        ide = League.objects.get(id=11)
        if len(data[i]['tt']) > 0:
            obj = Word.objects.update_or_create(
                language = ide,
                word = data[i]['tt'],
                code = data[i]["code"],
                image = data[i]["filename"]
            )
            newWords += 1
        ide = League.objects.get(id=12)
        if len(data[i]['ky']) > 0:
            obj = Word.objects.update_or_create(
                language = ide,
                word = data[i]['ky'],
                code = data[i]["code"],
                image = data[i]["filename"]
            )
            newWords += 1
        ide = League.objects.get(id=13)
        if len(data[i]['uz']) > 0:
            obj = Word.objects.update_or_create(
                language = ide,
                word = data[i]['uz'],
                code = data[i]["code"],
                image = data[i]["filename"]
            )
            newWords += 1
        ide = League.objects.get(id=14)
        if len(data[i]['ug']) > 0:
            tbr = reshaper.reshape(data[i]['ug'])
            result = get_display(tbr)
            obj = Word.objects.update_or_create(
                language = ide,
                word = result,
                code = data[i]["code"],
                image = data[i]["filename"]
            )
            newWords += 1
    msg = f"Added {newLanguages} new languages and {newWords} new words."
    return HttpResponse(msg, content_type='text/plain')

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

#
# This function lists the high scores of all users
#
def high_scores(request):
    # Loads user profiles from the database
    users = UserProfile.objects.all()
    paginator = Paginator(users, 10)
    
    page_number = request.GET.get('page')
    user_scores = paginator.get_page(page_number)

    # loads all scores from the languages table
    languages = LanguageScore.objects.all()

    # Passes the data to the front end
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
    try:
        usEngCorr = round(usEnglish["total"] / usEnglish["frequency"] *100,1)
    except:
        usEngCorr = 0
    ukEnglish = Word.objects.filter(language=2).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    
    try:
        ukEngCorr = round(get_average_correct(ukEnglish["total"], ukEnglish["frequency"]),2)
    except:
        ukEngCorr = 0

    tr = Word.objects.filter(language=3).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    try:
        trCorr = round(get_average_correct(tr["total"],tr["frequency"]),2)
    except:
        trCorr = 0

    ar = Word.objects.filter(language=4).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    try:
        arCorr = round(get_average_correct(ar["total"], ar["frequency"]),2)
    except:
        arCorr = 0

    az = Word.objects.filter(language=5).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    try:
        azCorr = round(get_average_correct(az["total"], az["frequency"]),)
    except:
        azCorr = 0

    ur = Word.objects.filter(language=6).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    try:
        urCorr = round(get_average_correct(ur["total"],ur["frequency"]),)
    except:
        urCorr = 0

    ot = Word.objects.filter(language=7).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    try:
        otCorr = round(get_average_correct(ot["total"],ot["frequency"]),)
    except:
        otCorr = 0

    kt = Word.objects.filter(language=8).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    try:
        ktCorr = round(get_average_correct(kt["total"],kt["frequency"]),)
    except:
        ktCorr = 0

    kk = Word.objects.filter(language=9).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    try:
        kkCorr = round(get_average_correct(kk["total"],kk["frequency"]),)
    except:
        kkCorr = 0
    tk = Word.objects.filter(language=10).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    try:
        tkCorr = round(get_average_correct(tk["total"],tk["frequency"]),)
    except:
        tkCorr = 0

    tt = Word.objects.filter(language=11).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    try:
        ttCorr = round(get_average_correct(tt["total"],tt["frequency"]),)
    except:
        ttCorr = 0

    ky = Word.objects.filter(language=12).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    try:
        kyCorr = round(get_average_correct(ky["total"],ky["frequency"]),)
    except:
        kyCorr = 0
    uz = Word.objects.filter(language=13).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    try:
        uzCorr = round(get_average_correct(uz["total"],uz["frequency"]),)
    except:
        uzCorr = 0

    ug = Word.objects.filter(language=14).aggregate(total= Sum('correctAnswerCount'), frequency= Sum('frequency'))
    try:
        ugCorr = round(get_average_correct(ug["total"],ug["frequency"]),)
    except:
        ugCorr = 0
    all_words_easiest = Word.objects.filter(frequency__gt=0).order_by("-correctAnswerCount").annotate(perc=Sum(F("correctAnswerCount")/F("frequency")*100))[:10]

    
    all_words_hardest = Word.objects.filter(frequency__gt=0).annotate(perc=Sum(F("correctAnswerCount")/F("frequency")*100)).order_by("perc", )[:10]
    
    
    data = {
        0:{"language":"Azeri","attempts":az["frequency"], "correctAnswers":azCorr},
        1:{"language":"US English","attempts":usEnglish["frequency"], "correctAnswers":usEngCorr},
        2:{"language":"UK English","attempts":ukEnglish["frequency"], "correctAnswers":ukEngCorr},
        3:{"language":"Turkish","attempts":tr["frequency"], "correctAnswers":trCorr},
        4:{"language":"Arabic","attempts":ar["frequency"], "correctAnswers":arCorr},
        5:{"language":"Urdu","attempts":ur["frequency"], "correctAnswers":urCorr},
        6:{"language":"Ottoman Turkish","attempts":ot["frequency"], "correctAnswers":otCorr},
        7:{"language":"Cypriot Turkish","attempts":kt["frequency"], "correctAnswers":ktCorr},
        8:{"language":"Kazakh","attempts":kk["frequency"], "correctAnswers":kkCorr},
        9:{"language":"Turkmen","attempts":tk["frequency"], "correctAnswers":tkCorr},
        10:{"language":"Tatar","attempts":tt["frequency"], "correctAnswers":ttCorr},
        11:{"language":"Kirghiz","attempts":ky["frequency"], "correctAnswers":kyCorr},
        12:{"language":"Uzbek","attempts":uz["frequency"], "correctAnswers":uzCorr},
        13:{"language":"Uyghur","attempts":ug["frequency"], "correctAnswers":ugCorr},
    }
    res = sorted(data, key=lambda x: (data[x]['attempts']), reverse=True)
    
    stats = {}
    
    for r in range(0,len(res)):
        try:
            perTotalQs = ((data[res[r]]["attempts"]/frequency['total'])*100)
        except:
            perTotalQs = 0
        dict1 = {r:{
            "language":data[res[r]]["language"],
            "attempts":data[res[r]]["attempts"],
            "correctAnswers":data[res[r]]["correctAnswers"],
            "perOfTotalQs":perTotalQs,
            }}
        stats.update(dict1)

    context = {
        "correct":correct, "inCorr_perc":inCorr_perc,"corr_per":corr_per, "incorrect":incorrect,
        "stats":stats, "awe":all_words_easiest,"awh":all_words_hardest,
                }
    return render(request, 'game/stats.html', context)

def attribution_p(request):

    context = {}

    return render(request, 'game/attr.html', context)
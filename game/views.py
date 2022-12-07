from django.shortcuts import render
from .models import League, Word
from random import shuffle
import json

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

def play_us(request):
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
        "clue":correct_word
    }
    return render(request, 'game/game_template.html', context)
import json, sys
import arabic_reshaper
from bidi.algorithm import get_display

# Opening JSON file
with open('file_dict.json', encoding="utf8") as f:
    data = json.load(f) 

def reshaped_text(x):
    res = arabic_reshaper.reshape(x)
    return get_display(res)

i = 20
print(f'English: {data[i]["us"]}\nTurkish: {data[i]["tr"]}\nArabic: {reshaped_text(data[i]["ar"])}')
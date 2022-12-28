import json, sys
import arabic_reshaper
from bidi.algorithm import get_display

# Opening JSON file
# r'C:\path\to\your\filename.ext'
# r'c:\Coding\Django_Babadum_Clone\game\file_dict.json'
with open('file_dict.json', encoding="utf8") as f:
    data = json.load(f) 

def reshaped_text(x):
    res = arabic_reshaper.reshape(x)
    return get_display(res)

# i = 20
# print(f'English: {data[i]["us"]}\nTurkish: {data[i]["tr"]}\nArabic: {reshaped_text(data[i]["ar"])}')

d = []
for i in data:
    try:
        i["ot"]
        x = i["ot"]
    except:
        x = ""
    dict = {
        "code": i["code"],
        "filename": i["filename"],
        "us": i["us"],
        "uk": i["uk"],
        "ar":reshaped_text(i["ar"]), # arabic
        "tr":i["tr"], # turkce
        "az":i["az"], # azeri
        "ur":reshaped_text(i["ur"]), # urdu
        "ot":x, # ottoman
        "kt":"", # kibris turkcesi
        "kk":"", # kazakh
        "tk":"", # turkmen
        "tt":"", # tatar
        "ky":"", # kirghiz
        "uz":"", # uzbek
        "ug":"" # uyghur
    }
    d.append(dict)

# # Serializing json
json_object = json.dumps(d, indent=4)
 
# # Writing to sample.json
with open("words_file.json", "w") as outfile:
    outfile.write(json_object)
from deep_translator import GoogleTranslator
import json, sys
import arabic_reshaper
from bidi.algorithm import get_display
ar_configuration = {
    'delete_harakat': False,
    'support_ligatures': True,
    'RIAL SIGN': True,  # Replace ر ي ا ل with ﷼
}

reshaper = arabic_reshaper.ArabicReshaper(configuration=ar_configuration)

# Opening JSON file
with open('words_file.json', encoding="utf8") as f:
    data = json.load(f) 

from bidi import algorithm


def trans(text, g_src, g_dest):
    ar = GoogleTranslator(source=g_src, target=g_dest).translate(text)
    if g_dest == "ur":
        tbr = reshaper.reshape(ar)
        result = get_display(tbr)
        ar = result
    else:  
        text = ar #.encode("utf-8")
        # ar = sys.stdout.buffer.write(text)
    return ar

lenofdata = len(data)
for i in range(0, len(data)):
    perc = round((i / lenofdata) * 100,2)
    print(f"{data[i]['us']} ... len is {len(data[i]['us'])} ... {perc}%")
    # if len(data[i]["ar"]) ==0:
    #     try:
    #         ar = trans(data[i]["us"], "en", "ar")
    #         data[i]["ar"] = ar
    #         print(f'US: {data[i]["us"]}, AR: {ar}')
    #     except:
    #         t = len(data[i]["ar"])
    #         print(f"Failed to translate US:{data[i]['us']} in to Arabic\n{data[i]['ar']} --> len of word {t}")
    # if len(data[i]["tr"]) ==0:
    #     try:
    #         tr = trans(data[i]["us"], "en", "tr")
    #         data[i]["tr"] = tr
    #         print(f'US: {data[i]["us"]}, TR: {tr}')
    #     except:
    #         t = len(data[i]["tr"])
    #         print(f"Failed to translate US: {data[i]['us']} in to Turkish\n{data[i]['tr']} --> len of word {t}")
    if len(data[i]["az"]) ==0:
        try:
            az = trans(data[i]["tr"], "tr", "az")
            data[i]["az"] = az
            print(f'US: {data[i]["us"]}, TR: {data[i]["tr"]}, AZ: {az}')
        except:
            t = len(data[i]["az"])
            print(f"Failed to translate TR: {data[i]['tr']} in to Azeri\n{data[i]['az']} --> len of word {t}")
    if len(data[i]["ur"]) ==0:
        try:
            ur = trans(data[i]["tr"], "tr", "ur")
            data[i]["ur"] = ur
            print(f'US: {data[i]["us"]}, TR: {data[i]["tr"]}, ur: {ur}')
        except:
            t = len(data[i]["az"])
            print(f"Failed to translate TR: {data[i]['tr']} in to Azeri\n{data[i]['az']} --> len of word {t}")

# # Serializing json
json_object = json.dumps(data, indent=4)
 
# # Writing to sample.json
with open("file_dict.json", "w") as outfile:
    outfile.write(json_object)
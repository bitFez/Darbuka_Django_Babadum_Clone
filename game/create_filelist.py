import os, json

# Open a file
path = "media/"
dirs = os.listdir(path)

words = []

# This would print all the files and directories
for file in dirs:
    filename = file
    code, rest = file.split(" ", 1)
    name, extension = rest.split(".")
    dict = {"code": code, "filename":filename, "us":name, "uk":"", "ar":"", "tr":""}
    words.append(dict)

# f = open("file_dict.txt", "w")
# for i in words:
with open('file_dict.json', 'a') as f:
    f.write(json.dumps(words))
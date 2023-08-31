import json
from random import *
from spacyfunctions import *

lang = input("Choose a language from Portuguese, Korean, or Chinese: ")
print('Input Received: ' + str(lang))
difficulty = int(input("Choose a difficulty: 1 for beginner, 2 for intermediate, 3 for advanced: "))
print('Input Received: ' + str(difficulty))
if difficulty == 1:
    importfile = lang + 'begdata.json'
elif difficulty == 2:
    importfile = lang + 'interdata.json'
elif difficulty == 3:
    importfile = lang + 'advdata.json'


with open('./databases/' + importfile) as rf:
    dict = json.load(rf)

options = ""

for topic in dict:
    options = options + '\n' + str(topic)

genre = input("Input the topic you would like to receive: " + options + "\n")

index = randint(0, len(dict[genre])-1)
passage = dict[genre][index]

posIncluded = True
if lang == 'korean':
    print(koreanGen(posIncluded, passage))
elif lang == 'chinese:':
    print(chineseGen(posIncluded, passage))
elif lang == 'portuguese':
    print(portugueseGen(posIncluded, passage))
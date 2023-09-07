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

#genre = input("Input the topic you would like to receive: " + options + "\n")

#index = randint(0, len(dict[genre])-1)
for genre in dict:
    passages = dict[genre]
    print(genre + ": \n")
    if len(passages) > 0:
        for index in range(len(passages)):
            print('Passage ' + str(index+1) + ':\n')
            passage = passages[index] 
            passage.replace("\n", "")
            # posIncluded = True
            if lang == 'korean':
                print('a: ' + koreanGen(False, passage) + '\n')
                print('b: ' + koreanGen(True, passage) + '\n')
            elif lang == 'chinese':
                print(chineseGen(False, passage) + '\n')
                print(chineseGen(True, passage) + '\n')
            elif lang == 'portuguese':
                print(portugueseGen(True, passage) + '\n')
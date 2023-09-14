import json
from random import randint
import time
import spacyfunctions as sf

#Welcome to the pipeline! Everything should work when running this main file.

languages = [
    'Chinese',
    'Japanese',
    'Korean',
    'Spanish',
    'French',
    'Portuguese',
    'Russian',
    'German'
]

difficulties = [
    'Beginner',
    'Intermediate',
    'Advanced'
]

lang = input(f"Choose a language from {', '.join(languages)}: ")
print('Input Received: ' + lang)
lang.lower()
difficulty = input(f"Choose a difficulty from {', '.join(difficulties)}: ")
print('Input Received: ' + difficulty)
difficulty.lower()

importfile = f'{lang}Passages.json'

with open(f'./passage-databases/{importfile}') as rf:
    dict = json.load(rf)

genres = list(dict[difficulty].keys())

num = int(input('Please select an option: \nINPUT 1: Random C-test\nINPUT 2: Random C-Test from selected genre\nINPUT 3: All passages within a selected difficulty and genre converted to C-tests in input language\nINPUT 4: All passages in all genres within a selected difficulty converted to C-tests in input language\nINPUT 5: All passages converted to C-tests in input language\n'))
num2 = int(input('INPUT 1: Terminal\nINPUT 2: .txt\n'))
if num == 1:
    while True: 
        gIndex = randint(0, len(genres)-1)
        genre = genres[gIndex]
        if len(dict[difficulty][genre]) > 0:
            break
    index = randint(0, len(dict[difficulty][genre])-1) 
    passage = dict[difficulty][genre][index]
    if num2 == 1:
        sf.printAllTypes(passage, lang)
    elif num2 == 2:
        t = time.localtime()
        mod = f'{str(t.tm_year)}-{str(t.tm_mon)}-{str(t.tm_mday)}_{str(t.tm_hour)}-{str(t.tm_min)}'
        file = open(f'./testfiles/ctest{mod}', 'w')
        sf.writeAllTypes(passage, lang, file)
elif num == 2:
    while True:
        genre = input(f"Please choose a genre from {', '.join(genres)}: ")
        if len(dict[difficulty][genre]) > 0:
            break
        else:
            print(f'{genre} is empty! Please try again')
    index = randint(0, len(dict[difficulty][genre])-1)
    passage = dict[difficulty][genre][index]
    if num2 == 1:
        sf.printAllTypes(passage, lang)
    elif num2 == 2:
        t = time.localtime()
        mod = f'{str(t.tm_year)}-{str(t.tm_mon)}-{str(t.tm_mday)}_{str(t.tm_hour)}-{str(t.tm_min)}'
        file = open(f'./testfiles/ctest{mod}', 'w')
        sf.writeAllTypes(passage, lang, file)
elif num == 3:
    while True:
        genre = input(f"Please choose a genre from {', '.join(genres)}: ")
        if len(dict[difficulty][genre]) > 0:
            break
        else:
            print(f'{genre} is empty! Please try again')
    for index in range(len(dict[difficulty][genre])):
        print(f'Passage Group {index+1}:\n')
        passage = dict[difficulty][genre][index]
        if num2 == 1:
            sf.printAllTypes(passage, lang)
        elif num2 == 2:
            t = time.localtime()
            mod = f'{str(t.tm_year)}-{str(t.tm_mon)}-{str(t.tm_mday)}_{str(t.tm_hour)}-{str(t.tm_min)}'
            file = open(f'./testfiles/ctest{mod}', 'w')
            sf.writeAllTypes(passage, lang, file)
elif num == 4:
    for genre in dict[difficulty]:
        passages = dict[difficulty][genre]
        print(genre + ":\n")
        if len(passages) > 0:
            for index in range(len(passages)):
                print(f'Passage Group {index+1}:\n')
                passage = passages[index]
                if num2 == 1:
                    sf.printAllTypes(passage, lang)
                elif num2 == 2:
                    t = time.localtime()
                    mod = f'{str(t.tm_year)}-{str(t.tm_mon)}-{str(t.tm_mday)}_{str(t.tm_hour)}-{str(t.tm_min)}'
                    file = open(f'./testfiles/ctest{mod}', 'w')
                    sf.writeAllTypes(passage, lang, file)
elif num == 5:
    for difficulty in dict:
        print(difficulty + ":\n")
        for genre in dict[difficulty]:
            passages = dict[difficulty][genre]
            print(genre + ":\n")
            if len(passages) > 0:
                for index in range(len(passages)):
                    print(f'Passage Group {index+1}:\n')
                    passage = passages[index]
                    if num2 == 1:
                        sf.printAllTypes(passage, lang)
                    elif num2 == 2:
                        t = time.localtime()
                        mod = f'{str(t.tm_year)}-{str(t.tm_mon)}-{str(t.tm_mday)}_{str(t.tm_hour)}-{str(t.tm_min)}'
                        file = open(f'./testfiles/ctest{mod}', 'w')
                        sf.writeAllTypes(passage, lang, file)

# for difficulty in dict:
#     for genre in dict[difficulty]:
#         passages = dict[difficulty][genre]
#         print(genre + ": \n")
#         if len(passages) > 0:
#             for index in range(len(passages)):
#                 print('Passage ' + str(index+1) + ':\n')
#                 passage = passages[index] 
#                 passage.replace("\n", "")
#                 # posIncluded = True
#                 if lang == 'korean':
#                     print('a: ' + sf.koreanGen(False, passage) + '\n')
#                     print('b: ' + sf.koreanGen(True, passage) + '\n')
#                 elif lang == 'chinese':
#                     print(sf.chineseGen(False, passage) + '\n')
#                     print(sf.chineseGen(True, passage) + '\n')
#                 elif lang == 'portuguese':
#                     print(sf.portugueseGen(True, passage) + '\n')
#                 elif lang == 'japanese':
#                     print(sf.japaneseGen(True, passage) + '\n')
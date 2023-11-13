import json
from random import randint
import spacyfunctions as sf
import os

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
num2 = int(input('INPUT 1: Terminal\nINPUT 2: .txt\nINPUT 3: h5p content'))
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
        mod = sf.fileTimeMod()
        file = open(f'./testfiles/ctest{mod}', 'w')
        sf.writeAllTypes(passage, lang, file)
    elif num2 == 3:
        mod = sf.fileTimeMod()
        with open('./h5pdev/content-template.json', 'r') as f:
            d = json.loads(f.read())
        ctest = sf.testGen(passage, lang)
        d["questions"] = ctest
        path = f'./h5pdev/ctests/sample{mod}'
        os.mkdir(path)
        with open(f'.{path}/content.json', "x") as wf:
            json.dump(d, wf)
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
        mod = sf.fileTimeMod()
        file = open(f'./testfiles/ctest{mod}', 'w')
        sf.writeAllTypes(passage, lang, file)
    elif num2 == 3:
        mod = sf.fileTimeMod()
        with open('./h5pdev/content-template.json', 'r') as f:
            d = json.loads(f.read())
        d["questions"] = passage
        path = f'./h5pdev/ctests/sample{mod}'
        os.mkdir(path)
        with open(f'./h5pdev/ctests/content.json', "x") as wf:
            json.dump(d, wf)
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
            mod = sf.fileTimeMod()
            file = open(f'./testfiles/ctest{mod}', 'w')
            sf.writeAllTypes(passage, lang, file)
        elif num2 == 3:
            mod = sf.fileTimeMod()
            with open('./h5pdev/content-template.json', 'r') as f:
                d = json.loads(f.read())
            d["questions"] = passage
            path = f'./h5pdev/ctests/sample{mod}'
            os.mkdir(path)
            with open(f'./h5pdev/ctests/content.json', "x") as wf:
                json.dump(d, wf)
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
                    mod = sf.fileTimeMod()
                    file = open(f'./testfiles/ctest{mod}', 'w')
                    sf.writeAllTypes(passage, lang, file)
                elif num2 == 3:
                    mod = sf.fileTimeMod()
                    with open('./h5pdev/content-template.json', 'r') as f:
                        d = json.loads(f.read())
                    d["questions"] = passage
                    path = f'./h5pdev/ctests/sample{mod}'
                    os.mkdir(path)
                    with open(f'./h5pdev/ctests/content.json', "x") as wf:
                        json.dump(d, wf)
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
                        mod = sf.fileTimeMod()
                        file = open(f'./testfiles/ctest{mod}', 'w')
                        sf.writeAllTypes(passage, lang, file)
                    elif num2 == 3:
                        mod = sf.fileTimeMod()
                        with open('./h5pdev/content-template.json', 'r') as f:
                            d = json.loads(f.read())
                        d["questions"] = passage
                        path = f'./h5pdev/ctests/sample{mod}'
                        os.mkdir(path)
                        with open(f'./h5pdev/ctests/content.json', "x") as wf:
                            json.dump(d, wf)
elif num == 6:
    counter = 0
    for genre in dict[difficulty]:
        passages = dict[difficulty][genre]
        print(genre + ":\n")
        if len(passages) > 0:
            for index in range(len(passages)):
                print(f'Passage Group {index+1}:\n')
                passage = passages[index]
                print(passage)
                with open('./h5pdev/content-template.json', 'r') as f:
                        d = json.loads(f.read())
                d["questions"] = sf.testGen(passage, lang)
                path = f'./h5pdev/ctests/{lang[:4]}0{counter}'
                os.mkdir(path)
                with open(f'{path}/content.json', "x") as wf:
                    json.dump(d, wf)
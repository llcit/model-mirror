import json
import spacyfunctions as sf
import os

with open(f'./passage-databases/portuguesePassages.json') as rf:
    dict = json.load(rf)
counter = 0
for difficulty in dict:
        for genre in dict[difficulty]:
            passages = dict[difficulty][genre]
            if len(passages) > 0:
                for index in range(len(passages)):
                    counter = counter + 1
                    passage = passages[index]
                    with open('./h5pdev/content-template.json', 'r') as f:
                        d = json.loads(f.read())
                    ctest = sf.portugueseGen(passage)
                    d["questions"] = [ctest]
                    path = f'./h5pdev/ctests/port{counter}'
                    os.mkdir(path)
                    with open(f'{path}/content.json', "x") as wf:
                        json.dump(d, wf)
                    

# with open(f'.{path}/content.json', "x") as wf:
#     json.dump(d, wf)
import json
from random import *

with open("promptdatabase.json", "r") as rf:
    dict = json.load(rf)

userWants = 'Culture'

if userWants == 'Culture':
    index = randint(0, len(dict["Culture"])-1)
    passage = dict["Culture"][index]

print(passage)
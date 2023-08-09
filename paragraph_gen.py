import openai
import json
import os  # used to read in environment variable

APIKEY = os.environ['OPENAI_API_KEY']
openai.api_key = APIKEY

with open('paragraphmaterial.txt', 'r') as f:
    cinput = f.read()

language = 'korean'
text = 'QUERY: generate 5 new, extremely unique 110-word passages with differing word choice in' + language + ' about this exerpt: ' + cinput + '. Every passage must be in korean.'
initInstruction = 'You are a creative language teacher tasked with developing 5 unique 110 word passages in korean for the purpose of language instruction. These passages will be used to test language learners with their corresponding literacy levels. Separate each passage with a new line.'

def returnPrompts(sysinput, cinput):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
        {"role": "system", "content": sysinput},
        {"role": "user", "content": cinput}],
        temperature=0.2,
    )
    passages = response['choices'][0]['message']['content']
    return passages

passages = returnPrompts(initInstruction, cinput)
print("PASSAGES: " + passages)

#diff definitions of difficulty
intro = 'You are a writer tasked with modifying a set of passages to a set of instructions. These are the instructions: '
beginnerInstruction = 'Modify the following passages to beginner level korean, which means the language used has short sentences, simple grammar patterns, and uses vocabulary words of high frequency. If it is not in korean, translate it. Always put #### before every passage generated. Do not number or label the passages.'
intermediateInstruction = 'Modify the following passages to intermediate level korean, which means that the language used has somewhat complex grammar, more infrequent vocabulary, and longer sentences, but does not contain extremely complex grammar, jargon, or complex sentences. Always put #### before every passage generated. Do not number or label the passages.'
advancedInstruction = 'Modify the following passages to advanced level, which means that the language used has complex grammar, contains infrequent vocabulary words and jargon, and has lengthy sentences. Always separate every passage that is generated with #### as a delimiter Do not number or label the passages.'

difficulty = int(input("difficulty level, 1 for beginner, 2 for intermediate, 3 for advanced: "))
print('Input Received: ' + str(difficulty))
if difficulty == 1:
    userInput = intro + beginnerInstruction
    importfile = 'krbegdata.json'
elif difficulty == 2:
    userInput = intro + intermediateInstruction
    importfile = 'krinterdata.json'
else:
    userInput = intro + advancedInstruction
    importfile = 'kradvdata.json'

#simplification
def simplifyReplies(sysinput, cinput):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
        {"role": "system", "content": sysinput},
        {"role": "user", "content": cinput}],
        temperature=0,
    )
    passage = response['choices'][0]['message']['content']
    return passage

finalPassages = simplifyReplies(userInput, passages)

#split into array indices
arr = finalPassages.split("####")

for i in range(len(arr)):
    print(finalPassages)


def classifyPassages(cinput):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
        {"role": "user", "content": cinput}],
        max_tokens=100,
        temperature=0,
    )
    passage = response['choices'][0]['message']['content']
    return passage


with open(importfile, "r") as rf:
    dict = json.load(rf)

for i in range(len(arr)):
    if len(arr[i]) <= 200 and arr[i] == arr[-1]:
        break
    elif len(arr[i]) <= 200:
        arr[i] = arr[i+1]
    pintro = 'QUERY: Classify this passage in english as one of the following - Culture, Astronomy, School, Food, Sports, or Other. Give a one word response. Pick ONLY from these categories.' + arr[i]
    classification = classifyPassages(pintro)
    print(classification)
    if 'Culture' in classification:
        dict["Culture"].append(arr[i])
    elif 'Astronomy' in classification:
        dict["Astronomy"].append(arr[i])
    elif 'School' in classification:
        dict["School"].append(arr[i])
    elif 'Food' in classification:
        dict["Food"].append(arr[i])
    elif 'Sports' in classification:
        dict["Sports"].append(arr[i])
    else:
        dict["Other"].append(arr[i])

with open(importfile, "w") as wf:
    json.dump(dict, wf)
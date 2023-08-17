import openai
import json
import os  # used to read in environment variable

APIKEY = os.environ['OPENAI_API_KEY']
openai.api_key = APIKEY

def returnPrompts(sysinput, cinput):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
        {"role": "system", "content": sysinput},
        {"role": "user", "content": cinput}],
        temperature=0.5,
    )
    passages = response['choices'][0]['message']['content']
    return passages

def simplifyReplies(sysinput, cinput):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
        {"role": "system", "content": sysinput},
        {"role": "user", "content": cinput}],
        temperature=0,
    )
    passages = response['choices'][0]['message']['content']
    return passages

def classifyPassages(cinput):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
        {"role": "user", "content": cinput}],
        max_tokens=100,
        temperature=0
    )
    passages = response['choices'][0]['message']['content']
    return passages

with open('paragraphmaterial.txt', 'r') as f:
    cinput = f.read()\

cinput = ''.join(cinput.splitlines())
text = 'QUERY: write FIVE unique, distinct 110-word passages with differing word choice from this source material: ' + cinput + '. Do not directly copy this material, you may use your own sources if necessary. Do not label the passages AT ALL. Each passage should talk about different parts of the sample text in more detail.'
initInstruction = "You are a creative language teacher tasked with writing 5 unique and creative 200 word passages for the purpose of language instruction. Separate every passage with #### as a delimiter, always do this. Do not copy the source material. Do not label the passages with 'Passage 1' or anything similar. Do not start or end the list of passages with the delimiter."

basePassages = returnPrompts(initInstruction, text)
print(basePassages)
basePassages = basePassages.split("####")
basePassages.pop(0)
#basePassages.pop(len(basePassages)-1)

language = input('Please select a language: english, korean, portuguese, or chinese: ')
intro = 'You are a language teacher tasked with modifying a given set of paragraphs to a set of instructions. Only include the passages in the response.'
beginnerInstruction = 'Beginner level ' + language + ' means the language used has short sentences, simple grammar patterns, and uses vocabulary words of high frequency. Most importantly, it must be very easy to read and understand. The length of the passage should be the equivalent of 100 english words.'
intermediateInstruction = 'Modify the following passages to intermediate level ' + language + ' which means that the language used has somewhat complex grammar, more infrequent vocabulary, and longer sentences, but does not contain extremely complex grammar, jargon, or complex sentences.'
advancedInstruction = 'Modify the following passages to advanced level ' + language + ' , which means that the language used has complex grammar, contains infrequent vocabulary words and jargon, and has lengthy sentences.'

basecinput =  'Modify this passage to beginner level ' + language + '. Do not include anything other than the following passage:'

difficulty = int(input("difficulty level, 1 for beginner, 2 for intermediate, 3 for advanced: "))
print('Input Received: ' + str(difficulty))
if difficulty == 1:
    userInput = intro + beginnerInstruction
    importfile = language + 'begdata.json'
elif difficulty == 2:
    userInput = intro + intermediateInstruction
    importfile = language + 'interdata.json'
else:
    userInput = intro + advancedInstruction
    importfile = language + 'advdata.json'

finalPassages = []

with open(importfile, "r") as rf:
    dict = json.load(rf)
    
for i in range(len(basePassages)):
    finalPassages.append(simplifyReplies(userInput,(basecinput + basePassages[i])))
    finalPassages[i] = ''.join(finalPassages[i].splitlines())
    print(finalPassages[i])
    pintro = 'QUERY: Classify this passage in english as one of the following - Culture, Astronomy, School, Food, Sports, or Other. Give a one word response. Pick ONLY from these categories.' + finalPassages[i]
    classification = classifyPassages(pintro)
    print(classification)
    if 'Culture' in classification:
        dict["Culture"].append(finalPassages[i])
    elif 'Astronomy' in classification:
        dict["Astronomy"].append(finalPassages[i])
    elif 'School' in classification:
        dict["School"].append(finalPassages[i])
    elif 'Food' in classification:
        dict["Food"].append(finalPassages[i])
    elif 'Sports' in classification:
        dict["Sports"].append(finalPassages[i])
    else:
        dict["Other"].append(finalPassages[i])

with open(importfile, "w") as wf:
    json.dump(dict, wf)
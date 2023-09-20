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

language = input('Please select a language: english, korean, portuguese, or chinese: ')
language = language.lower()
intro = 'You are a multilingual language expert tasked with modifying a sample passage to a set of instructions. Only include the passages in the response.'
beginnerInstruction = f'Modify the passage to beginner level {language}. Beginner level means the language used has short sentences, simple grammar patterns, and uses vocabulary words of high frequency. Most importantly, it must be very easy to read and understand. The length of the passage should be the equivalent of 100 english words. Do not include anything other than the resulting passage.'
intermediateInstruction = f'Modify the following passages to intermediate level {language} which means that the language used has somewhat complex grammar, more infrequent vocabulary, and longer sentences, but does not contain extremely complex grammar, jargon, or complex sentences.'
advancedInstruction = f'Modify the following passages to advanced level {language} , which means that the language used has complex grammar, contains infrequent vocabulary words and jargon, and has lengthy sentences.'

basecinput =  f'Modify this passage to beginner level {language}. Do not include anything other than the following passage:'

difficulty = int(input("difficulty level, 1 for beginner, 2 for intermediate, 3 for advanced: "))
print('Input Received: ' + str(difficulty))
if difficulty == 1:
    userInput = beginnerInstruction
    difficulty = 'beginner'
elif difficulty == 2:
    userInput = intermediateInstruction
    difficulty = 'intermediate'
else:
    userInput = advancedInstruction
    difficulty = 'advanced'

cinput = ''.join(cinput.splitlines())
text = 'QUERY: write FIVE unique, distinct 110-word passages with differing word choice from this source material: ' + cinput + '. Do not directly copy this material, you may use your own sources if necessary. Do not label the passages AT ALL. Each passage should talk about different parts of the sample text in more detail.'
initInstruction = "You are a creative linguist tasked with writing 5 " + difficulty + "-level, unique and creative 110 word passages. You MUST use " + difficulty + "-level vocabulary and syntax. Separate every passage with #### as a delimiter, always do this. Do not copy the source material. Do not label the passages with 'Passage 1' or anything similar. Do not start or end the list of passages with the delimiter."

basePassages = returnPrompts(initInstruction, text)
print(basePassages)
basePassages = basePassages.split("####")
basePassages.pop(0)

importfile = f'{language}Passages.json'

finalPassages = []

with open('./passage-databases/'+ importfile, "r") as rf:
    dict = json.load(rf)
    
for i in range(len(basePassages)):
    finalPassages.append(simplifyReplies(intro, (userInput + basePassages[i])))
    finalPassages[i] = ''.join(finalPassages[i].splitlines())
    pintro = f'QUERY: Classify this passage in english. Pick ONLY from these categories and only respond with that category as a response: "history, math, popculture, fiction, language, sports, business, science, or other {finalPassages[i]}.'
    classification = classifyPassages(pintro)
    classification.lower()
    dict[difficulty][classification].append(finalPassages[i])

with open('./passage-databases/' + importfile, "w") as wf:
    json.dump(dict, wf)
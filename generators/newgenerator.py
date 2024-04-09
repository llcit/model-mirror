from openai import OpenAI
import json
import os  # used to read in environment variable

APIKEY = os.environ['OPENAI_API_KEY']
ORG = os.environ['ORGANIZATION']
client = OpenAI()


def returnPrompts(sysinput, cinput):
    response = client.chat.completions.create(
        model='gpt-4-turbo-preview',
        messages=[
        {"role": "system", "content": sysinput},
        {"role": "user", "content": cinput}],
        temperature=0.5,
    )
    passages = response.choices[0].message.content
    return passages

def simplifyReplies(sysinput, cinput):
    response = client.chat.completions.create(
        model='gpt-4-turbo-preview',
        messages=[
        {"role": "system", "content": sysinput},
        {"role": "user", "content": cinput}],
        temperature=0,
    )
    passages = response.choices[0].message.content
    return passages

def classifyPassages(cinput):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
        {"role": "user", "content": cinput}],
        max_tokens=100,
        temperature=0
    )
    passages = response.choices[0].message.content
    return passages

with open('paragraphmaterial.txt', 'r') as f:
    cinput = f.read()\

language = input('Please select a language: english, korean, portuguese, or chinese: ')
language = language.lower()
intro = 'You are a multilingual language expert tasked with modifying a sample passage to a set of instructions. Only include the passages in the response.'
CEFRA2Instruction = f'Modify the passage to CEFRA2 level {language}. CEFR A2 level means that you can write short, simple notes and messages relating to matters in areas of immediate needs. You can write a very simple personal letter, for example thanking someone for something. The length of the passage should be the equivalent of 100 english words. Do not include anything other than the resulting passage.'
CEFRB1Instruction = f'Modify the following passages to CEFRB1 level {language}. CEFR B1 level means that you can write simple connected text on topics which are familiar or of personal interest. You can write personal letters describing experiences and impressions. The length of the passage should be the equivalent of 100 english words. Do not include anything other than the resulting passage.'
CEFRB2Instruction = f'Modify the following passages to CEFRB2 level {language}. CEFR B2 level means that you can write clear, detailed text on a wide range of subjects related to my interests. You can write an essay or report, passing on information or giving reasons in support of or against a particular point of view. You can write letters highlighting the personal significance of events and experiences. The length of the passage should be the equivalent of 100 english words. Do not include anything other than the resulting passage.'

difficulty = int(input("difficulty level, 1 for CEFRA2, 2 for CEFRB1, 3 for CEFRB2: "))
print('Input Received: ' + str(difficulty))
if difficulty == 1:
    userInput = CEFRA2Instruction
    difficulty = 'CEFRA2'
    ddifficulty = 'beginner'
elif difficulty == 2:
    userInput = CEFRB1Instruction
    difficulty = 'CEFRB1'
    ddifficulty = 'intermediate'
else:
    userInput = CEFRB2Instruction
    difficulty = 'CEFRB2'
    ddifficulty = 'advanced'

cinput = ''.join(cinput.splitlines())
text = 'QUERY: write FIVE unique, distinct 110-word passages with differing word choice from this source material: ' + cinput + '. Do not directly copy this material, you may use your own sources if necessary. Do not label the passages AT ALL. Each passage should talk about different parts of the sample text.'
initInstruction = "You are a creative linguist tasked with writing 5 " + ddifficulty + "-level, unique and creative 110 word passages. You MUST use " + ddifficulty + "-level vocabulary and syntax. Separate every passage with #### as a delimiter, always do this. Do not copy the source material. Do not label the passages with 'Passage 1' or anything similar. Do not start or end the list of passages with the delimiter."

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
    dict[ddifficulty][classification].append(finalPassages[i])

with open('./passage-databases/' + importfile, "w") as wf:
    json.dump(dict, wf)
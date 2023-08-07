import fitz
import openai
import json

APIKEY = 'examplekey'
openai.api_key = APIKEY

#select the language you want
language = 'english'

try:
    #pdf file input
    doc = fitz.open("IntangibleCulturalHeritageandNewTechnologies.pdf")
except SystemError:
    print("error opening pdf")
else:
    #reads pdf page uploads in sequence
    c = ''
    for page in doc.pages(2,doc.page_count,1):
        if(len(c) < 40000):
            extract = page.get_text()
            c += extract
doc.close()

#changes number of passages based on text length
num = int(len(c)/10000) + 3
print(num)
numPassages = str(num)
text = 'QUERY: write ' + numPassages + ' extremely unique 120-word passages with differing word choice in' + language + ' about this exerpt: ' + c + '. \n\n Each passage should be about a different concept discussed in the excerpt.'
initInstruction = 'You are a language teacher tasked with developing unique 120 word passages for the purpose of language instruction. These passages will be used to test language learners with their corresponding literacy levels. Generate' + numPassages + ' unique passages as a base for this learning process.'

#returns the base passages
def returnPassages(sysinput, cinput):
    if len(cinput) <= 16200:
        response = openai.ChatCompletion.create(
        #model
        model='gpt-3.5-turbo',
        #system and content inputs
        messages=[
        {"role": "system", "content": sysinput},
        {"role": "user", "content": cinput}],
        max_tokens=1000,
        #changes the randomness
        temperature=0   
    )
    else:
        response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo-16k',
        messages=[
        {"role": "system", "content": sysinput},
        {"role": "user", "content": cinput}],
        max_tokens=1000,
        temperature=0   
    )
    reply = response['choices'][0]['message']['content']
    return reply

reply = returnPassages(initInstruction, text)

#diff definitions of difficulty
intro = 'You are a writer tasked with modifying a set of passages to a set of instructions. These are the instructions: '
beginnerInstruction = 'Simplify the following passages to beginner level, which means the language used has short sentences, simple grammar patterns, and uses vocabulary words of high frequency. Always separate every passage that is generated with #### as a delimiter. Do not put a delimiter before the first passage.'
intermediateInstruction = 'Modify the following passages to intermediate level, which means that the language used has somewhat complex grammar, more infrequent vocabulary, and longer sentences, but does not contain extremely complex grammar, jargon, or complex sentences. Always separate every passage that is generated with #### as a delimiter. Do not put a delimiter before the first passage.''
advancedInstruction = 'Modify the following passages to advanced level, which means that the language used has complex grammar, contains infrequent vocabulary words and jargon, and has lengthy sentences. Always separate every passage that is generated with #### as a delimiter. Do not put a delimiter before the first passage.''

userInput = intro + beginnerInstruction

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

finalPassages = simplifyReplies(userInput, reply)

#if you want to store into file
with open('FULLRUNTEST.txt', 'a') as f:
    f.write('\n\nSYSTEM PROMPT: ' + initInstruction + '\n\n')
    f.write('QUERY: write 3 200-word passages in english about this exerpt: \n\n')
    f.write('TEXT INPUT: ' + text + '\n\n')
    f.write('RESPONSE: ' + reply + '\n\n')
    f.write('QUERY 2: ' + userInput + '\n\n')
    f.write('Final Passsages' + finalPassages)

#split into array indices
arr = finalPassages.split("####")

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

with open("promptdatabase.json", "r") as rf:
    dict = json.load(rf)

for i in range(len(arr)):
    pintro = 'QUERY: Classify this passage as one of the following - Culture, Astronomy, School, Food, Sports, or Other' + arr[i]
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

with open("promptdatabase.json", "w") as wf:
    json.dump(dict, wf)

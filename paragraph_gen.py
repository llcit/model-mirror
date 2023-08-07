import openai

APIKEY = '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'
openai.api_key = APIKEY

initInstruction = 'You are a writer tasked with creating 5 120-word passages based on a paragraph of source material. You may draw from other sources in this writing.'

with open('paragraphmaterial.txt', 'r') as f:
    cinput = f.read()

cinput = 'QUERY: Write 5 unique 120-word passages based loosely on this paragraph: ' + cinput

def returnPrompts(sysinput, cinput):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
        {"role": "system", "content": sysinput},
        {"role": "user", "content": cinput}],
        max_tokens=1000,
        temperature=0.9,
        presence_penalty = 0.8
    )
    reply = response['choices'][0]['message']['content']
    return reply

passages = returnPrompts(initInstruction, cinput)

with open('paragenresponse.txt', 'a') as f:
    f.write('\n\nSYSTEM PROMPT: ' + initInstruction + '\n\n')
    f.write(cinput + '\n\n')
    f.write('TEXT INPUT: ' + passages + '\n\n')
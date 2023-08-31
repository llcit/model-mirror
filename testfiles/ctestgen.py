import nltk

text = "We need to learn more about intersectionality to really understand it. We can't just have simple ideas about what it means. We need to look at its history and think about it carefully. By doing this, we can see how important intersectionality is and how it can help us make things better."
lemm = nltk.WordNetLemmatizer()
sentences = nltk.sent_tokenize(text)
ctestfinal = ""

def convert(input):
    base = ""
    print(str(input) + '\n')
    for i in range(len(input)):
        if (i == 0):
            base += (' ' + input[i] + ' ')
        elif (input[i] != input[-1]) and ("'" in input[i+1]):
            base += input[i]
        elif (input[i] != input[-1]) and (',' in input[i+1]):
            base += input[i]
        elif (input[i] != input[-1]) and ('.' in input[i+1]):
            base += input[i]
        elif (input[i] != input[-1]):
            base += (input[i] + ' ')
        else:
            base += input[i]
    return base

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words[1] = lemm.lemmatize(words[1])
    newword, trash = divmod(len(words[1]), 2)
    words[1] = words[1][:newword + trash]
    words[1] += ("_" * newword)
    sentences[i] = words
    conversion = convert(sentences[i])
    ctestfinal += conversion

ctestfinal = ctestfinal.lstrip(" ")
print(ctestfinal)
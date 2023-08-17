import spacy

nlp = spacy.load('pt_core_news_lg')

doc = nlp("A suposi\u00e7\u00e3o de que explicar estrat\u00e9gias matem\u00e1ticas verbalmente garantir\u00e1 a compreens\u00e3o dos alunos \u00e9 falha, como argumentam Kling e Bay-Williams. Uma mera explica\u00e7\u00e3o \u00e9 insuficiente; os alunos precisam de tempo e experi\u00eancias para realmente entender e visualizar as rela\u00e7\u00f5es num\u00e9ricas. Em vez disso, os educadores devem fazer amplo uso de estrat\u00e9gias visuais, como sugerido pelos pesquisadores. Uma atividade divertida envolve cart\u00f5es de Olhada R\u00e1pida, onde os alunos s\u00e3o brevemente mostrados grupos de pontos ou imagens de itens familiares. Eles s\u00e3o ent\u00e3o solicitados a determinar a quantidade e como a perceberam. Ao representar n\u00fameros visualmente, seja atrav\u00e9s de pontos ou manipulativos, os alunos podem obter uma compreens\u00e3o mais profunda dos princ\u00edpios subjacentes das estrat\u00e9gias matem\u00e1ticas.Outra ferramenta visual eficaz \u00e9 Splat!, uma cria\u00e7\u00e3o de Steve Wyborney. Essa atividade envolve contar pontos em slides e depois revelar um slide com uma grande mancha cobrindo alguns pontos. Os alunos s\u00e3o desafiados a determinar quantos pontos est\u00e3o escondidos pela mancha. Atrav\u00e9s desse exerc\u00edcio, os alunos desenvolvem suas pr\u00f3prias estrat\u00e9gias, como contar para cima ou para baixo e utilizar a voz ou os dedos. Incentivar o pensamento independente promove uma compreens\u00e3o mais s\u00f3lida dos conceitos matem\u00e1ticos.Al\u00e9m disso, Kling e Bay-Williams enfatizam a import\u00e2ncia de ensinar fatos de adi\u00e7\u00e3o e multiplica\u00e7\u00e3o em uma ordem espec\u00edfica. Em vez de come\u00e7ar com 0 e 1, eles recomendam come\u00e7ar com conjuntos fundamentais como 2, 10 e 5. Esses conjuntos n\u00e3o s\u00e3o apenas mais familiares para os alunos, mas tamb\u00e9m servem como base para derivar outros fatos matem\u00e1ticos. Ao dominar conjuntos fundamentais, os alunos podem decompor problemas complexos e lidar com c\u00e1lculos mais desafiadores. Depois, os alunos podem progredir para quadrados, que s\u00e3o \u00fateis para estudos futuros em \u00e1lgebra, geometria e medi\u00e7\u00e3o.")
assert doc.has_annotation("SENT_START")
base = ""

#every word w token.pos >2 gap astrix before+after gap
for sent in doc.sents:
    counter = 1
    nounFound = False
    for token in sent:
        if counter%2 == 0 and nounFound is False and len(token.shape_) > 1:
            ttoken = str(token)
            newword, trash = divmod(len(ttoken), 2)
            ttoken = " " + ttoken[:newword] + "*" + ttoken[newword:] + "*" + "(" + token.pos_ + ")"
            #nounFound = True
        elif token.pos_ == 'PUNCT':
            ttoken = str(token)
        else:
            ttoken = " " + str(token)
        counter = counter + 1
        base = base + ttoken
        
base = base.lstrip(' ')
print(doc.text + '\n\n')
print(base)

#print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#        token.shape_, token.is_alpha, token.is_stop)
#    print('\n\n\n')
# + "(" + token.pos_ + ")"
import spacy

nlp = spacy.load('ko_core_news_lg')

doc = nlp(u"\uc77c\ubcf8\uc758 \uc804\ud1b5 \uc5f0\uadf9\uc5d0\uc11c \ubc30\uc6b0\ub4e4\uc740 \ub180\ub77c\uc6b4 \ubcc0\uc2e0\uc744 \ud569\ub2c8\ub2e4. \uadf8\ub4e4\uc740 \uac00\uba74, \uac00\ubc1c, \uadf8\ub9ac\uace0 \uc758\uc0c1\uc744 \uc0ac\uc6a9\ud558\uc5ec \uc678\ubaa8\ub97c \ubc14\uafc9\ub2c8\ub2e4. \uc608\ub97c \ub4e4\uc5b4, \ub299\uc740 \ub0a8\uc790\ub294 \uc80a\uc740 \uc2e0\uc774 \ub418\uac70\ub098 \uc544\ub984\ub2e4\uc6b4 \uc5ec\uc790\ub294 \uc804\uc0ac\uc758 \uc720\ub839\uc774 \ub420 \uc218 \uc788\uc2b5\ub2c8\ub2e4. \ud55c\ud3b8, \ub2e4\ub978 \ubc30\uc6b0\uc778 '\uc544\uc774'\ub294 \ud604\uc9c0 \uc0ac\ub78c\uc744 \ub9cc\ub098\uc11c \uc6c3\uc74c\uc744 \uc81c\uacf5\ud569\ub2c8\ub2e4. \uc544\uc774\ub294 \uc720\ub839\uc758 \uc804\uc124\uc744 \ud655\uc778\ud558\uace0 \ub2e4\ub978 \ubc30\uc6b0\uc5d0\uac8c \uadf8 \uc601\ud63c\uc744 \uc704\ud574 \uae30\ub3c4\ud558\ub77c\uace0 \uc81c\uc548\ud569\ub2c8\ub2e4. \uadf8 \ud6c4, \ubcc0\uc2e0\ud55c \ubc30\uc6b0\uac00 \ubb34\ub300\uc5d0 \ub2e4\uc2dc \ub098\ud0c0\ub0a9\ub2c8\ub2e4.")
assert doc.has_annotation("SENT_START")
base = ""
for sent in doc.sents:
    nounFound = False
    for token in sent:
        if token.pos_ == 'NOUN' and nounFound is False:
            token = " NOUN"
            nounFound = True
        elif token.pos_ == 'PUNCT':
            token = str(token)
        else:
            token = " " + str(token)
        base = base + token
        
base = base.lstrip(' ')
print(doc.text + '\n\n')
print(base)
#        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#                token.shape_, token.is_alpha, token.is_stop)
#    print('\n\n\n')
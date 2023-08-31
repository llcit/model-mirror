import spacy

def chineseGen(posIncluded, passage):
    nlp = spacy.load(passage)
    doc = nlp(passage)
    assert doc.has_annotation("SENT_START")
    base = ""
    sentcounter = 1
    #every word w token.pos >2 gap astrix before+after gap
    for sent in doc.sents:
        counter = 1
        for token in sent:
            if counter%2 == 0 and len(token.shape_) > 1 and sentcounter != 1:
                if token.pos_ != 'PROPN' and token.pos_ != 'NUM':
                    ttoken = str(token)
                    newword, trash = divmod(len(ttoken), 2)
                    ttoken = ttoken[:newword] + "*" + ttoken[newword:] + "*" + "(" + token.pos_ + ")"
                else:
                    ttoken = str(token)
            elif token.pos_ == 'PUNCT':
                ttoken = str(token) + " "
            else:
                ttoken = str(token)
            counter = counter + 1
            base = base + ttoken
        sentcounter = sentcounter + 1
            
    base = base.lstrip(' ')
    #print(doc.text + '\n\n')
    return base

def koreanGen(posIncluded, passage):
    nlp = spacy.load('ko_core_news_lg')
    doc = nlp(passage)
    assert doc.has_annotation("SENT_START")
    base = ""
    sentencecounter = 1
    for sent in doc.sents:
        counter = 1
        for token in sent:
            if counter%2 == 0 and len(token.shape_) > 1 and sentencecounter != 1:
                ttoken = str(token)
                if token.pos_ != 'X' and token.pos_ != 'NUM' and token.pos_ != 'PROPN' and (('a' or 'e' or 'i' or 'u' or 'y' or 'o') not in ttoken):
                    newword, trash = divmod(len(ttoken), 2)
                    if posIncluded is True:
                        ttoken = " " + ttoken[:newword] + "*" + ttoken[newword:] + "*" + "(" + token.pos_ + ")"
                    else:
                        ttoken = " " + ttoken[:newword] + "*" + ttoken[newword:] + "*"
                else:
                    ttoken = " " + ttoken
            elif token.pos_ == 'PUNCT':
                ttoken = str(token)
            else:
                ttoken = " " + str(token)
            counter = counter + 1
            base = base + ttoken
        sentencecounter = sentencecounter + 1
    base = base.lstrip(' ')
    return base

def portugueseGen(posIncluded, passage):
    nlp = spacy.load('pt_core_news_lg')
    doc = nlp(passage)
    assert doc.has_annotation("SENT_START")
    base = ""
    sentcounter = 1
    #every word w token.pos >2 gap astrix before+after gap
    for sent in doc.sents:
        counter = 1
        for token in sent:
            if counter%2 == 0 and len(token.shape_) > 1 and sentcounter != 1:
                ttoken = str(token)
                if token.pos_ != 'PROPN' and token.pos_ != 'NUM':
                    newword, trash = divmod(len(ttoken), 2)
                    if posIncluded is True:
                        ttoken = " " + ttoken[:newword] + "*" + ttoken[newword:] + "*" + "(" + token.pos_ + ")"
                    else:
                        ttoken = " " + ttoken[:newword] + "*" + ttoken[newword:] + "*"
                else:
                    ttoken = " " + ttoken
            elif token.pos_ == 'PUNCT':
                ttoken = str(token)
            else:
                ttoken = " " + str(token)
            counter = counter + 1
            base = base + ttoken
        sentcounter = sentcounter + 1
            
    base = base.lstrip(' ')
    #print(doc.text + '\n\n')
    return base
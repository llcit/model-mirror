import spacy

#standard c-tests
def testGen(passage, language, posIncluded=False, lenExclude=1, freq=2, posExclude=['PROPN', 'NUM', 'X', 'SPACE']):
    if language == 'chinese':
        nlp = spacy.load('zh_core_web_trf')
        doc = nlp(passage)
        assert doc.has_annotation("SENT_START")
        base = ""
        sentcounter = 1
        #every word w token.pos >2 gap astrix before+after gap
        for sent in doc.sents:
            counter = 1
            for token in sent:
                if counter%freq == 0 and len(token.shape_) > lenExclude and sentcounter != 1:
                    if token.pos_ not in posExclude and (('a' or 'e' or 'i' or 'u' or 'y' or 'o') not in ttoken):
                        ttoken = str(token)
                        newword, trash = divmod(len(ttoken), 2)
                        if posIncluded == True:
                            ttoken = f'{ttoken[:newword]}*{ttoken[newword:]}*({token.pos_})'
                        else:
                            ttoken = ttoken[:newword] + "*" + ttoken[newword:] + "*"
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
    elif language == 'korean':
        nlp = spacy.load('ko_core_news_lg')
        doc = nlp(passage)
        assert doc.has_annotation("SENT_START")
        base = ""
        sentencecounter = 1
        for sent in doc.sents:
            counter = 1
            for token in sent:
                if counter%freq == 0 and len(token.shape_) > lenExclude and sentencecounter != 1:
                    ttoken = str(token)
                    if token.pos_ not in posExclude and (('a' or 'e' or 'i' or 'u' or 'y' or 'o') not in ttoken):
                        newword, trash = divmod(len(ttoken), 2)
                        if posIncluded is True:
                            ttoken = f' {ttoken[:newword]}*{ttoken[newword:]}*({token.pos_})'
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
    elif language == 'portuguese':
        nlp = spacy.load('pt_core_news_lg')
        doc = nlp(passage)
        assert doc.has_annotation("SENT_START")
        base = ""
        sentcounter = 1
        #every word w token.pos >2 gap astrix before+after gap
        for sent in doc.sents:
            counter = 1
            for token in sent:
                if counter%freq == 0 and len(token.shape_) > lenExclude and sentcounter != 1:
                    ttoken = str(token)
                    if token.pos_ not in posExclude:
                        newword, trash = divmod(len(ttoken), 2)
                        if posIncluded is True:
                            ttoken = f' {ttoken[:newword]}*{ttoken[newword:]}*({token.pos_})'
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
    elif language == 'french':
        nlp = spacy.load('fr_dep_news_trf')
        doc = nlp(passage)
        assert doc.has_annotation("SENT_START")
        base = ""
        sentcounter = 1
        #every word w token.pos >2 gap astrix before+after gap
        for sent in doc.sents:
            counter = 1
            for token in sent:
                if counter%freq == 0 and len(token.shape_) > lenExclude and sentcounter != 1:
                    ttoken = str(token)
                    if token.pos_ not in posExclude:
                        newword, trash = divmod(len(ttoken), 2)
                        if posIncluded is True:
                            ttoken = f' {ttoken[:newword]}*{ttoken[newword:]}*({token.pos_})'
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
    elif language == 'german':
        nlp = spacy.load('de_dep_news_trf')
        doc = nlp(passage)
        assert doc.has_annotation("SENT_START")
        base = ""
        sentcounter = 1
        #every word w token.pos >2 gap astrix before+after gap
        for sent in doc.sents:
            counter = 1
            for token in sent:
                if counter%freq == 0 and len(token.shape_) > lenExclude and sentcounter != 1:
                    ttoken = str(token)
                    if token.pos_ not in posExclude:
                        newword, trash = divmod(len(ttoken), 2)
                        if posIncluded is True:
                            ttoken = f' {ttoken[:newword]}*{ttoken[newword:]}*({token.pos_})'
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
    elif language == 'russian':
        nlp = spacy.load('ru_core_news_lg')
        doc = nlp(passage)
        assert doc.has_annotation("SENT_START")
        base = ""
        sentcounter = 1
        #every word w token.pos >2 gap astrix before+after gap
        for sent in doc.sents:
            counter = 1
            for token in sent:
                if counter%freq == 0 and len(token.shape_) > lenExclude and sentcounter != 1:
                    ttoken = str(token)
                    if token.pos_ not in posExclude:
                        newword, trash = divmod(len(ttoken), 2)
                        if posIncluded is True:
                            ttoken = f' {ttoken[:newword]}*{ttoken[newword:]}*({token.pos_})'
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
    elif language == 'spanish':
        nlp = spacy.load('es_dep_news_trf')
        doc = nlp(passage)
        assert doc.has_annotation("SENT_START")
        base = ""
        sentcounter = 1
        #every word w token.pos >2 gap astrix before+after gap
        for sent in doc.sents:
            counter = 1
            for token in sent:
                if counter%freq == 0 and len(token.shape_) > lenExclude and sentcounter != 1:
                    ttoken = str(token)
                    if token.pos_ not in posExclude:
                        newword, trash = divmod(len(ttoken), 2)
                        if posIncluded is True:
                            ttoken = f' {ttoken[:newword]}*{ttoken[newword:]}*({token.pos_})'
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
    elif language == 'japanese':
        nlp = spacy.load('ja_core_news_trf')
        doc = nlp(passage)
        assert doc.has_annotation("SENT_START")
        base = ""
        sentcounter = 1
        #every word w token.pos >2 gap astrix before+after gap
        for sent in doc.sents:
            counter = 1
            for token in sent:
                if counter%freq == 0 and len(token.shape_) > lenExclude and sentcounter != 1:
                    ttoken = str(token)
                    if token.pos_ not in posExclude:
                        newword, trash = divmod(len(ttoken), 2)
                        if posIncluded is True:
                            ttoken = f'{ttoken[:newword]}*{ttoken[newword:]}*({token.pos_})'
                        else:
                            ttoken = ttoken[:newword] + "*" + ttoken[newword:] + "*"
                    else:
                        ttoken = str(token)
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

#return basic C-tests in language-specific functions
def chineseGen(passage):
    return testGen(passage, 'chinese')

def koreanGen(passage):
    return testGen(passage, 'korean')

def portugueseGen(passage):
    return testGen(passage, 'portuguese')

def frenchGen(passage):
    return testGen(passage, 'french')

def germanGen(passage):
    return testGen(passage, 'german')

def russianGen(passage):
    return testGen(passage, 'russian')

def spanishGen(passage):
    return testGen(passage, 'spanish')

def japaneseGen(passage):
    return testGen(passage, 'japanese')

#Print all tests to terminal
def printAllTypes(passage, lang):
    ctestPos = testGen(passage, lang, True)
    ctestnPos = testGen(passage, lang, False)
    print(f'Original Passage:\n{passage}\n')
    print(f'C-Test (No Parts of Speech):\n{ctestnPos}\n')
    print(f'C-Test (Parts of Speech):\n{ctestPos}')

#Print all tests to file
def writeAllTypes(passage, lang, file):
    ctestPos = testGen(passage, lang, True)
    ctestnPos = testGen(passage, lang, False)
    file.write(f'Original Passage:\n{passage}\n')
    file.write(f'C-Test (No Parts of Speech):\n{ctestnPos}\n')
    file.write(f'C-Test (Parts of Speech):\n{ctestPos}')

#deletes whole words
def modularGen(passage, language, posIncluded=False, lenExclude=1, freq=2, posExclude=['PROPN', 'NUM']):
    if language == 'portuguese':
        nlp = spacy.load('pt_core_news_lg')
        doc = nlp(passage)
        assert doc.has_annotation("SENT_START")
        base = ""
        sentcounter = 1
        #every word w token.pos >2 gap astrix before+after gap
        for sent in doc.sents:
            counter = 1
            for token in sent:
                if counter%freq == 0 and len(token.shape_) > lenExclude and sentcounter != 1:
                    ttoken = str(token)
                    if token.pos_ not in posExclude:
                        newword, trash = divmod(len(ttoken), 2)
                        if posIncluded is True:
                            ttoken = f' {ttoken[:newword]}*{ttoken[newword:]}*({token.pos_})'
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
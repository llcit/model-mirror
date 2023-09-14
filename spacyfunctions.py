import spacy

def languageGen(posIncluded, passage, language):
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
                if counter%2 == 0 and len(token.shape_) > 1 and sentcounter != 1:
                    if token.pos_ != 'PROPN' and token.pos_ != 'NUM':
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
                if counter%2 == 0 and len(token.shape_) > 1 and sentencecounter != 1:
                    ttoken = str(token)
                    if token.pos_ != 'X' and token.pos_ !='SPACE' and token.pos_ != 'NUM' and token.pos_ != 'PROPN' and (('a' or 'e' or 'i' or 'u' or 'y' or 'o') not in ttoken):
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
                if counter%2 == 0 and len(token.shape_) > 1 and sentcounter != 1:
                    ttoken = str(token)
                    if token.pos_ != 'PROPN' and token.pos_ != 'NUM':
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
                if counter%2 == 0 and len(token.shape_) > 1 and sentcounter != 1:
                    ttoken = str(token)
                    if token.pos_ != 'PROPN' and token.pos_ != 'NUM':
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
                if counter%2 == 0 and len(token.shape_) > 1 and sentcounter != 1:
                    ttoken = str(token)
                    if token.pos_ != 'PROPN' and token.pos_ != 'NUM':
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
                if counter%2 == 0 and len(token.shape_) > 1 and sentcounter != 1:
                    ttoken = str(token)
                    if token.pos_ != 'PROPN' and token.pos_ != 'NUM':
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
                if counter%2 == 0 and len(token.shape_) > 1 and sentcounter != 1:
                    ttoken = str(token)
                    if token.pos_ != 'PROPN' and token.pos_ != 'NUM':
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
                if counter%2 == 0 and len(token.shape_) > 1 and sentcounter != 1:
                    ttoken = str(token)
                    if token.pos_ != 'PROPN' and token.pos_ != 'NUM':
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

def chineseGen(posIncluded, passage):
    nlp = spacy.load('zh_core_web_trf')
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
                if token.pos_ != 'X' and token.pos_ !='SPACE' and token.pos_ != 'NUM' and token.pos_ != 'PROPN' and (('a' or 'e' or 'i' or 'u' or 'y' or 'o') not in ttoken):
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

def frenchGen(posIncluded, passage):
    nlp = spacy.load('fr_dep_news_trf')
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

def germanGen(posIncluded, passage):
    nlp = spacy.load('de_dep_news_trf')
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

def russianGen(posIncluded, passage):
    nlp = spacy.load('ru_core_news_lg')
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

def spanishPassages(posIncluded, passage):
    nlp = spacy.load('es_dep_news_trf')
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

def japaneseGen(posIncluded, passage):
    nlp = spacy.load('ja_core_news_trf')
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

def printAllTypes(passage, lang):
    ctestPos = languageGen(True, passage, lang)
    ctestnPos = languageGen(False, passage, lang)
    print(f'Original Passage:\n{passage}\n')
    print(f'C-Test (No Parts of Speech):\n{ctestnPos}\n')
    print(f'C-Test (Parts of Speech):\n{ctestPos}')

def writeAllTypes(passage, lang, file):
    ctestPos = languageGen(True, passage, lang)
    ctestnPos = languageGen(False, passage, lang)
    file.write(f'Original Passage:\n{passage}\n')
    file.write(f'C-Test (No Parts of Speech):\n{ctestnPos}\n')
    file.write(f'C-Test (Parts of Speech):\n{ctestPos}')
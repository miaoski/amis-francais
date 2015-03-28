#-*- coding: utf8 -*-
# Convert txt/001.txt to dict-amis-p.json for moedict (p for Maurice Poinsot)

import sys
import re
import os
import json
import codecs

JSON = {}
INDEX = []

def tilde_words(s):
    return re.sub(r'([\w\']+)', r'`\1~', s)

def parse_title(s):
    "Possible formats: stem - word / word1 = word2 = word3 ... {category}"
    s = s.strip()
    category = re.search(r'{(\w+)}', s)
    cat = ''
    if category:
        cat = category.group(1)
        s = re.sub(r'{\w+}', '', s)     # Remove {F}, {Z}, etc.
    p = s.find(' - ')
    stem = ''
    if p != -1:                         # stem - word1 = word2 = ...
        stem = s[:p]
        s = s[p+3:]
    s = s.split(' = ')
    title = s[0].strip()
    link = s[1:]
    if stem != '':                      # add stem as the first synonym
        link = [stem, ] + link
    return (title, link, cat)

def mkword(title, definitions):
    global JSON, INDEX
    word = {'title': title,
        'heteronyms': [{'definitions': definitions}]}
    if title in JSON:
        print "Duplicated definition: " + title
    JSON[title] = word
    INDEX.append(title)

def mkdef(defi, examples, link, category):
    defdic = {}
    if len(examples) > 0:
        defdic['example'] = examples
        examples = []
    if defi != '':
        defdic['def'] = defi
    if category != '':
        defdic['type'] = category
    if link:
        defdic['synonyms'] = map(tilde_words, link)
    return defdic

def examplify(s):
    "\ufff9amis\ufffbfrançais"
    return u'\ufff9'+s[0]+u'\ufffb'+s[1]

def readdict(fn):
    fp = codecs.open(fn, mode = 'r', encoding = 'utf8')
    title = None
    state = 'N'
    num_words = 0
    for line in fp:
        l = line.rstrip()
        if l == '' and title:       # 寫入詞條
            num_words += 1
            defdic = mkdef(defi, examples, link, category)
            if len(defdic) > 0:
                definitions.append(defdic)
            mkword(title, definitions)
            title = None
            state = 'N'
            continue
        if l == '':                 # 空白行
            continue
        if l[0] == '#':             # 註解
            continue
        if state is 'N':            # 詞
            (title, link, category) = parse_title(l)
            definitions = []
            examples = []
            defi = ''
            state = 't'
            continue
        if l[0:2] == '=>':          # 相關詞
            syn = l[2:].lstrip().replace(', ', ',')
            link = link + syn.split(',')
            state = 'l'
            continue
        if l[0:2] == '- ':              # 阿美語例句
            ex[0] = l[2:]
            state = 'ea'
            continue
        if state == 'ea' and l[0:2] == '  ':          # 法文例句
            ex[1] = l[2:]
            examples.append(examplify(ex))
            ex = ['', '']
            state = 'ef'
            continue
        if state in ['t', 'f', 'ef']:   # 法文定義
            if defi != '':
                defdic = mkdef(defi, examples, link, category)
                definitions.append(defdic)
                examples = []
                link = None
            defi = l
            ex = ['', '']
            state = 'f'
            continue

    if title:
        num_words += 1
        defdic = mkdef(defi, examples, link, category)
        if len(defdic) > 0:
            definitions.append(defdic)
        mkword(title, definitions)
    fp.close()
    print 'Total %d words in %s' % (num_words, fn)


if __name__ == '__main__':
    for i in range(1, 3):
        readdict('./txt/%03d.txt' % i)
    f = codecs.open('index.json', mode='w', encoding='utf8')
    f.write(json.dumps(INDEX, indent=2, separators=(',', ':'), ensure_ascii = False))
    f.close()
    f = codecs.open('dict-amis-mp.json', mode='w', encoding='utf8')
    f.write(json.dumps(JSON.values(), indent=2, separators=(',', ':'), ensure_ascii = False))
    f.close()

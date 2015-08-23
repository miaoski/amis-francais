# -*- coding: utf8 -*-
# Extract lexicon from HOCR format

import os
import sys
from PIL import Image
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('toufu.sq3')
cur = conn.cursor()

page = sys.argv[1]
ocrfn = page + '.html'
imgfn = '../pic/' + page + '.jpg'
ocr = open(ocrfn).read()
im  = Image.open(imgfn)

try:
    os.mkdir(page)
except:
    pass

def canonical(t):
    t = t.replace('\u2014', '-') \
         .replace('\u2018', "'") \
         .replace(u'ﬁ', 'fi') \
         .replace(u'‘', "'") \
         .replace('\n', ' ')
    return t.strip()

bs = BeautifulSoup(ocr, 'html.parser')
for px in bs.find_all('p'):
    title = px.get('title')
    pid = px.get('id')
    txt = px.get_text()
    coords = [int(i) for i in title.split()[1:]]
    nim = im.crop(coords)
    nim.save('./%s/%s.jpg' % (page, pid))
    print '%d,%s,%s,%s' % (int(page), pid, title, canonical(txt))
    cur.execute('INSERT INTO toufu VALUES (?, ?, ?, ?)', (int(page), pid, title, canonical(txt)))
    conn.commit()

cur.close()

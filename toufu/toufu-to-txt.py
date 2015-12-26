import sqlite3
import codecs

conn = sqlite3.connect('toufu.sq3')
cur = conn.cursor()

for p in range(1,354):
    cur.execute('SELECT DISTINCT p,CAST(SUBSTR(par,5) AS INTEGER) AS par,ans FROM toufu WHERE p=? ORDER BY par', (p,))
    f = codecs.open('%03d.txt' % p, 'w', 'utf-8')
    for row in cur.fetchall():
        f.write(row[2] + '\n')
    f.close()

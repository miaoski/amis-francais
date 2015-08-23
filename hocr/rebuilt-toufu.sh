#!/bin/bash
rm toufu.sq3
sqlite3 toufu.sq3 < toufu.sql
for i in `seq -f%03g 1 353`; do
	python hocr2pars.py $i
done

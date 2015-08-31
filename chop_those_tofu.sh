#/bin/bash
git clone https://github.com/CindyLinz/StripPhotoIntoRows.git ../StripPhotoIntoRows
cd pic/
for i in `seq -f%03g 001 353`; do
    ../../StripPhotoIntoRows/cut_line $i.jpg;
    for n in cut_strip_*.jpg; do
        mv $n ../stripes/`echo $n | sed "s/cut_strip/$i/"`
    done
done

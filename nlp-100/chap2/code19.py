#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter
hoge = []
with open('hightemp.txt', 'r') as f:
    for line in f:
        elements = line.rstrip().split('\t')
        hoge.append(elements[0])
counter = Counter(hoge)
for word, cnt in counter.most_common():
    print (word, cnt)

#unixcommand
#cut -f 1 hightemp.txt | sort | uniq -c | sort -r  

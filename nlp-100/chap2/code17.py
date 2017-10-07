#!/usr/bin/env python
# -*- coding: utf-8 -*-
hoge = set()
with open('hightemp.txt', 'r') as f:
    for line in f:
        elements = line.rstrip().split('\t')
        for line in elements[0]:
            hoge.add(elements[0])
print(hoge)
#unixcommand
#cut -f 1 hightemp.txt | sort |  uniq

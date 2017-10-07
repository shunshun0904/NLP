#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter
data = []
fp = open("00-input.txt")
for line in fp:
    sentence = line.rstrip().split(" ")
    data.extend(sentence)
    counter = Counter(data)
for word, cnt in counter.most_common():
    print(word,cnt)

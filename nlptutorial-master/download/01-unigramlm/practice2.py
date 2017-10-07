#!/usr/bin/env python
# -*- coding: utf-8 -*-

for line in fp:
    sentence = line.rstrip().split(" ")
    data.extend(sentence)
    counter = Counter(data)
for word, cnt in counter.most_common():
    print(word,cnt)

from collections import Counter
total_count = 0
fp = open(../../test/"01-train-input.txt")
data = []
for line in fp:
    sentence = line.rstrip().split(" ")
    append “</s>” to the end of words 
    for each word in words
        add 1 to counts[word]
        a   dd 1 to total_count

open the model_file for writing
for each word, count in counts
probability = counts[word]/total_count
print word, probability to model_file

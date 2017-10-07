#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ngram(nlp,hoge):
    box = []
    for i in range(0,len(hoge)-nlp+1):
        box.append(hoge[i:nlp+i])
    return box
    
hoge = "I am an NLPer"
words_hoge = hoge.split(" ")

#単語バイグラム
box = ngram(2,words_hoge)
print(box)
#文字バイグラム
box = ngram(2,hoge)
print(box)
      
        
        
    
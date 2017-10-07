#!/usr/bin/env python
# -*- coding: utf-8 -*-


def ngram(nlp,hoge):
    box = []
    for i in range(0,len(hoge)-nlp+1):
        box.append(hoge[i:nlp+i])
    return box

hoge1 = "paraparaparadise"
hoge2 = "paragraph"
box = ngram(2,hoge1)
X = box
box = ngram(2,hoge2)
Y = box
X_set = set(X)
Y_set = set(Y)
print(X)
print(Y)
print ("se" in X)     # in: X に "se" が含まれていれば True, いなければ False
print ("se" in Y)     # ほとんど同上（X -> Y）
sum_list = list(X_set | Y_set)
print(sum_list)
matched_list = list(X_set & Y_set)
print(matched_list)
dif_list = list(X_set - Y_set)
print(dif_list)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

num_first_only = (0, 4, 5, 6, 7, 8, 14, 15, 18)
hoge = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
huga = hoge.split(" ")

result = {}
for (num, word) in enumerate(huga):
    if num in num_first_only:
        result[word[0:1]] = num
    else:
        result[word[0:2]] = num
print(result)       


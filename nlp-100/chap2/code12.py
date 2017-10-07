#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('hightemp.txt', 'r') as f:
    for line in f:
        elements = line.rstrip().split('\t')
        for line in elements[0:1]:
            with open('col1.txt', 'a') as  f:
                f.write(line + '\n')
        for line in elements[1:2]:
            with open('col2.txt', 'a') as  f:
                f.write(line + '\n') # 文字列の最後に改行を加えて1行ずつ書き込み

#UNIXcommand
#cut -f 2 hightemp.txt
#cut -f 1 hightemp.txt 

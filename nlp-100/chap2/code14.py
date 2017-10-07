#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
hoge = sys.argv[2]
with open(sys.argv[1]) as f:
    lines = f.readlines()
for line in lines[:int(hoge)]:
    print (line)


# head -10 hightemp.txt 

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
with open(sys.argv[1]) as f:
    lines = f.readlines()
for line in sorted(lines, key=lambda x: x.split()[2], reverse=True):
    print (line)
#unixcommand
#sort -r -k 3 hightemp.txt
# cat 3 hightemp.txt

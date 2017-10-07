#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import sys
hoge = sys.argv[2]
with open(sys.argv[1]) as f:
    lines = f.readlines()
count = len(lines)
unit = math.ceil(count / int(hoge))  # 1ファイル当たりの行数
for i, offset in enumerate(range(0, count, unit), 1):
    with open('child_{:02d}.txt'.format(i), mode='w') as out_file:
        for line in lines[offset:offset + unit]:
            out_file.write(line)
#unixcommand
#split -l 4 hightemp.txt out.

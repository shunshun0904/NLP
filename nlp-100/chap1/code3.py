#!/usr/bin/env python
# -*- coding: utf-8 -*-


str1 = list("パトカー")
str2 = list("タクシー")
s ="".join(a+b for (a, b) in zip("パトカー", "タクシー"))  #list1,list2を同時にループ
print(s)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import re

with open("jawiki-country.json") as f:
    article_json = f.readline()
    while article_json:
        article_dict = json.loads(article_json)
        if article_dict["title"] == "イギリス":
            lines = article_dict["text"].split("\n")
            for line in lines:
                if "Category" in line:
                    # 正規表現のコンパイル その2
                    pattern = re.compile(r'''
                        ^       # 行頭
                        .*      # 任意の文字0文字以上
                        \[\[Category:
                        (.*?)   # キャプチャ対象、任意の文字0文字以上、非貪欲マッチ
                        (?:\]\]|\|) # キャプチャ対象外、']]'または'|'
                        .*      # 任意の文字0文字以上
                        $       # 行末
                        ''', re.MULTILINE + re.VERBOSE)
                    # 抽出
                    result = pattern.findall(line)
                    print(result)
        article_json = f.readline()

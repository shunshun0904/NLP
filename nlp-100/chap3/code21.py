#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
with open("jawiki-country.json") as f:
    article_json = f.readline()
    while article_json:
        article_dict = json.loads(article_json)
        if article_dict["title"] == "イギリス":
            lines = article_dict["text"].split("\n")
            for line in lines:
                if "Category" in line:
                    print(line)
        article_json = f.readline()

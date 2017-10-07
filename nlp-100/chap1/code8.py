#!/usr/bin/env python
# -*- coding: utf-8 -*-


def origin(x,y,z):
    box = "{shun}時の{naka}は{ore}".format(shun = x, naka = y ,ore = z)
    return box
    
box = origin(12,"気温",22.4)
print(box)

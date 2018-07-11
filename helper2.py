#!/usr/bin/python
# -*- coding: utf-8 -*-


for line in open("rest.txt", 'r'):
    line = line.strip().split(' ')
    if not line[1].startswith('NEG='):
        print line[0] + "\t" + line[1]
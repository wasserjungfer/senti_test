#!/usr/bin/python
# -*- coding: utf-8 -*-


for line in open("SentiWS_v1.8c_Negative.txt", 'r'):
    line = line.strip().split('\t')
    print line[0] + '\t' + line[1]
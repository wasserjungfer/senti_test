#!/usr/bin/python
# -*- coding: utf-8 -*-

ws_pos = []
ws_numbers_pos = []
for line in open("SentiWS_Positive.txt", 'r'):
    line = line.split('\t')
    ws_pos.append(line[0].strip())
    ws_numbers_pos.append(line[1].strip())

ws_neg = []
ws_numbers_neg = []
for line in open("SentiWS_Negative.txt", 'r'):
    line = line.split('\t')
    ws_neg.append(line[0].strip())
    ws_numbers_neg.append(line[1].strip())

for line in open("corpus_annotated_3.tsv", 'r'):
    line = line.strip()
    lemma = line.split('\t')
    if len(lemma) < 3:#"<s>": #or "</s>":
        print line
        continue
    #print line
    the_lemma = lemma[2]
    if the_lemma in ws_pos:
        print line + '\t' + "POS" + ';' + ws_numbers_pos[ws_pos.index(the_lemma)]

    elif the_lemma in ws_neg:
        print line + '\t' + "NEG" + ';' + ws_numbers_neg[ws_neg.index(the_lemma)]

    else:
        print line + '\t' + "NULL"
#!/usr/bin/python
# -*- coding: utf-8 -*-

polart_pos = []
polart_numbers_pos = []
for line in open("POlart_pos.txt", 'r'):
    line = line.split('\t')
    polart_pos.append(line[0].strip())
    polart_numbers_pos.append(line[1].strip())

polart_neg = []
polart_numbers_neg = []
for line in open("POlart_neg.txt", 'r'):
    line = line.split('\t')
    polart_neg.append(line[0].strip())
    polart_numbers_neg.append(line[1].strip())

polart_neut = []
polart_numbers_neut = []
for line in open("POlart_neu.txt", 'r'):
    line = line.split('\t')
    polart_neut.append(line[0].strip())
    polart_numbers_neut.append(line[1].strip())

for line in open("corpus_annotated_2.tsv", 'r'):
    line = line.strip()
    lemma = line.split('\t')
    if len(lemma) < 3:#"<s>": #or "</s>":
        print line
        continue
    #print line
    the_lemma = lemma[2]
    if the_lemma in polart_pos:
        print line + '\t' + "POS" + ';' + polart_numbers_pos[polart_pos.index(the_lemma)]

    elif the_lemma in polart_neg:
        print line + '\t' + "NEG" + ';' + polart_numbers_neg[polart_neg.index(the_lemma)]

    elif the_lemma in polart_neut:
        print line + '\t' + "NEUT" + ';' + polart_numbers_neut[polart_neut.index(the_lemma)]

    else:
        print line + '\t' + "NULL"
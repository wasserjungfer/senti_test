#!/usr/bin/python
# -*- coding: utf-8 -*-



GermanPolarityClues_pos = []
GermanPolarityClues_numbers_pos = []
for line in open("GermanPolarityClues-Positive-Lemma-21042012.tsv", 'r'):
    line = line.split('\t')
    GermanPolarityClues_pos.append(line[0].strip())
    GermanPolarityClues_numbers_pos.append(line[4].strip())

GermanPolarityClues_neg = []
GermanPolarityClues_numbers_neg = []
for line in open("GermanPolarityClues-Negative-Lemma-21042012.tsv", 'r'):
    line = line.split('\t')
    GermanPolarityClues_neg.append(line[0].strip())
    GermanPolarityClues_numbers_neg.append(line[4].strip())

GermanPolarityClues_neut = []
GermanPolarityClues_numbers_neut = []
for line in open("GermanPolarityClues-Neutral-Lemma-21042012.tsv", 'r'):
    line = line.split('\t')
    GermanPolarityClues_neut.append(line[0].strip())
    GermanPolarityClues_numbers_neut.append(line[4].strip())


for line in open("corpus-annotated.tsv", 'r'):
    line = line.strip()
    lemma = line.split('\t')
    if len(lemma) < 3:#"<s>": #or "</s>":
        print line
        continue

    the_lemma = lemma[2]
    if the_lemma in GermanPolarityClues_pos:
        print line + '\t' + "POS" + ';' + GermanPolarityClues_numbers_pos[GermanPolarityClues_pos.index(the_lemma)]

    elif the_lemma in GermanPolarityClues_neg:
        print line + '\t' + "NEG" + ';' + GermanPolarityClues_numbers_neg[GermanPolarityClues_neg.index(the_lemma)]

    elif the_lemma in GermanPolarityClues_neut:
        print line + '\t' + "NEUT" + ';' + GermanPolarityClues_numbers_neut[GermanPolarityClues_neut.index(the_lemma)]

  #  elif the_lemma in morphcomp_neu:
  #      print line + '\t' + "neu"


    else:
        print line + '\t' + "NULL"


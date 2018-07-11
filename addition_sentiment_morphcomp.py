#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict

additional_polarity_morphcomp = defaultdict(list)
additional_polarity_POlart = defaultdict(list)
additional_polarity_GermanPolarityClues = defaultdict(list)
additional_polarity_SentiWS = defaultdict(list)

morphcomp_int = []
for line in open("morphcomp_int.txt", 'r'):
    morphcomp_int.append(line.strip())

morphcomp_pos = []
for line in open("morphcomp_pos.txt", 'r'):
    morphcomp_pos.append(line.strip())

morphcomp_neg = []
for line in open("morphcomp_neg.txt", 'r'):
    morphcomp_neg.append(line.strip())

morphcomp_neu = []
for line in open("morphcomp_neu.txt", 'r'):
    morphcomp_neu.append(line.strip())


for line in open("corpus_annotated_1.tsv", 'r'):
    line = line.strip()
    lemma = line.split('\t')
    if len(lemma) < 3:#"<s>": #or "</s>":
        print line
        continue
    #print line
    the_lemma = lemma[2]
    if the_lemma in morphcomp_int:
        print line + '\t' + "int"

    elif the_lemma in morphcomp_pos:
        print line + '\t' + "pos"

    elif the_lemma in morphcomp_neg:
        print line + '\t' + "neg"

    elif the_lemma in morphcomp_neu:
        print line + '\t' + "neu"


    else:
        print line + '\t' + "NULL"

#    print morphcomp

#with open("test_set.txt", 'w') as out:
    #for line in the_lemma:
        #if morphcomp == the_lemma:
            #print morphcomp
            #out.write(the_lemma + '\t' + morphcomp)
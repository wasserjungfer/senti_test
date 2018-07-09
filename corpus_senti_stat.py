#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import defaultdict
# top ten most positiv reviews (review is something between document<>, count "positives" inwithin those documents, sentence barrier not count),
# sentiments are the following rows: 11-  12-  13- 14-
# outwrite information by eaxh lexica (only taking into account row 11, or only row 12 or only row 13 etc.)
# outwrite information taking into account all the rows. Count +1 if there is a positive value at least at one of the rows.
# outwrite number of a review (hidden in doc_id  + sorted from the review with the highest numeber to the least number. + print the top 10 reviews)

# the same for the negatives.

# the same for the weights. Combine the weights: see row 11, row 13. Here count only separates.

# find the most often used positive and negative, neutral words.
# ourwrite all positive and negative words. Should count as positive or negative if at least on of the rows 11, 12, 13, 14 has a sentiment.

text = open('corpus_senti.tsv', 'r')
pos_count = defaultdict(int)
neg_count = defaultdict(int)
#positivewordfreq = []

for line in text:
    line = line.strip().split('\t')
    if len(line) <= 5:
        continue
    if line[11].startswith('POS') or line[12].startswith('pos') or line[13].startswith('POS') or line[14].startswith('POS'):
        #print line
        #print(line[2])
        pos_count[line[2]] += 1
    if line[11].startswith('NEG') or line[12].startswith('neg') or line[13].startswith('NEG') or line[14].startswith('NEG'):
        neg_count[line[2]] += 1
        if line[2] == 'kaufen':
            print line


pos_res = sorted(pos_count.items(), key=lambda pair: pair[1], reverse=True)
neg_res = sorted(neg_count.items(), key=lambda pair: pair[1], reverse=True)

#for pair in neg_res:
    #print pair
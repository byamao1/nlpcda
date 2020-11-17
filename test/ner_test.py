#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 14:22
# @Author  : Baiyu
# @File    : ner.py
from nlpcda import Ner

ner = Ner(ner_dir_name='../write',
          ignore_tag_list=['O', 'T'],
          data_augument_tag_list=['mobile'],
          augument_size=10, seed=0, delimiter=' ')
data_sentence_arrs, data_label_arrs = ner.augment('../write/mobile.txt')
# print(data_sentence_arrs, data_label_arrs)

with open('../write/augment_supplement_train.txt', 'w', encoding='utf-8') as f:
    for list_i in range(len(data_sentence_arrs)):
        for sentence, label in zip(data_sentence_arrs[list_i], data_label_arrs[list_i]):
            f.write(str(sentence) + " " + str(label) + "\n")
        f.write("\n\n")

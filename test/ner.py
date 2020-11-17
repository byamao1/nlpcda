#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 14:22
# @Author  : Baiyu
# @File    : ner.py
from nlpcda import Ner

ner = Ner(ner_dir_name='../write',
          ignore_tag_list=['O', 'T'],
          data_augument_tag_list=['organization'],
          augument_size=3, seed=0, delimiter=' ')
data_sentence_arrs, data_label_arrs = ner.augment('../write/train_0.txt')
print(data_sentence_arrs, data_label_arrs)

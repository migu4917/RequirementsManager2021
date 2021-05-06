import numpy as np
import pandas as pd
from typing import List, Dict
import re
import jieba


stop_words_set = set()


def _load_stop_words_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as stop_word_file:
        for line in stop_word_file:
            stop_words_set.add(line.rstrip())


def filter_stop_words(words: List) -> List:
    if len(stop_words_set) == 0:
        _load_stop_words_file('./static/哈工大停用词表.txt')

    def is_useful_word(word: str):
        s = word.strip()
        return len(s) > 0 and s not in stop_words_set and not re.match(r'(\d|\.)+(?!(\W))', s)

    return list(filter(is_useful_word, words))


def jieba_cut_comment(comment: str) -> List:
    # 判断一个unicode是否是汉字
    def is_chinese(uchar):
        return u'\u4e00' <= uchar <= u'\u9fa5'

    cut_result = []
    seg_list = jieba.lcut(comment)
    for seg in seg_list:
        seg = seg.lower()
        seg = re.sub(r'[\d_%]+', '', seg.strip())
        if not is_chinese(seg):
            continue
        cut_result.append(seg)
    return cut_result

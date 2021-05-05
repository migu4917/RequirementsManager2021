# -*- coding: utf-8 -*-
import jieba
import pandas as pd
import wordcloud
import platform
import base64
from typing import List
import re

# 黑体
_macos_font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
# 黑体
_windows_font_path = 'C:\\Windows\\Fonts\\simhei.ttf'

_temp_wordcloud_png_file_name = './static/temp_wordcloud_png_file.png'

stop_words_set = set()


def _load_stop_words_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as stop_word_file:
        for line in stop_word_file:
            stop_words_set.add(line.rstrip())


def _filter_stop_words(words: List) -> List:
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


def _list2wordcloud(comments_list: list):
    if platform.system() == "Windows":
        font_path = _windows_font_path
    elif platform.system() == "Darwin":
        font_path = _macos_font_path
    else:
        print("unsupport platform")
        font_path = None
    # prepare the word list
    words = []
    for comment in comments_list:
        words += _filter_stop_words(jieba_cut_comment(comment))
    # construct a new WordCloud with some specific configuration
    w = wordcloud.WordCloud(background_color=None, mode="RGBA",
                            font_path=font_path, max_words=120, collocations=False)
    # filter the stop words
    # generate
    w.generate(' '.join(words))
    w.to_file(_temp_wordcloud_png_file_name)
    return True


def png2base64(file_name):
    img = open(file_name, 'rb')
    img_read = img.read()
    img.close()
    return base64.b64encode(img_read).decode('utf-8')


def generateWordCloudBase64(file):
    # parse the df to list
    df = pd.read_csv(file, encoding='utf-8')
    # use the list to generate wordcloud picture

    if 'class' in df.columns:
        df = df[lambda x: x['class'] != 'best']

    # print(df.shape)
    # print(df.head())

    _list2wordcloud(df['comments'].to_list())

    return png2base64(_temp_wordcloud_png_file_name)


if __name__ == '__main__':
    comments = ['你好我好大家好',
                'wordcloud 库把词云当作一个WordCloud对象',
                '基本使用',
                '以WordCloud对象为基础，配置参数、加载文本、输出文件']
    res = _list2wordcloud(comments)
    # 400 * 200, about 56KB
    print(png2base64(_temp_wordcloud_png_file_name))

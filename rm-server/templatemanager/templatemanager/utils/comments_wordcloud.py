# -*- coding: utf-8 -*-
import jieba
import pandas as pd
import wordcloud
import platform
import base64

_macos_font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
_windows_font_path = ''

_temp_wordcloud_png_file_name = './temp_wordcloud_png_file.png'


def _list2wordcloud(comments_list: list):
    font_path = ''
    if platform.system() == "Windows":
        font_path = _windows_font_path
    elif platform.system() == "Darwin":
        font_path = _macos_font_path
    else:
        print("unsupport platform")
        font_path = None
    # construct a new WordCloud with some specific configuration
    w = wordcloud.WordCloud(background_color="white",
                            font_path=font_path)
    # prepare the word list
    words = []
    for comment in comments_list:
        words += jieba.lcut(comment)
    # filter the stop words
    # generate
    w.generate(' '.join(words))
    w.to_file(_temp_wordcloud_png_file_name)
    return True


def png2base64(file_name) -> str:
    img = open(file_name, 'rb')
    img_read = img.read()
    img.close()
    return base64.urlsafe_b64encode(img_read)


def generateWordCloudBase64(file):
    # parse the df to list
    df = pd.DataFrame(file)
    # use the list to generate wordcloud picture
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


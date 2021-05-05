import pickle
import numpy as np
import pandas as pd
from gensim.models import KeyedVectors
import time
from sklearn.neural_network import MLPClassifier
from typing import List, Dict
import re
import jieba

label_table = {'additional_cost': 0,
               'functional_complaint': 1,
               'compatibility_issue': 2,
               'crashing': 3,
               'feature_removal': 4,
               'feature_request': 5,
               'network_problem': 6,
               'privacy_and_ethical_issue': 7,
               'resource_heavy': 8,
               'response_time': 9,
               'user_interface': 10,
               'safety': 11,
               'installation_issue': 12,
               'traffic_wasting': 13,
               'content': 14,
               'update_issue': 15,
               'other': 16}

label_list = ['additional_cost', 'functional_complaint', 'compatibility_issue', 'crashing',
              'feature_removal', 'feature_request', 'network_problem', 'privacy_and_ethical_issue',
              'resource_heavy', 'response_time', 'user_interface', 'safety',
              'installation_issue', 'traffic_wasting', 'content', 'update_issue', 'other']

_tencent_file = \
    'd:\\RequirementsManager2021\\comments-crawler\\tecent_ailab_word2vec\\Tencent_AILab_ChineseEmbedding_2M.twv'
_wv_from_text = None
_MAX_WORD_COUNT = 2000000

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


def _tencent_embedding(comments: pd.Series) -> pd.DataFrame:
    global _wv_from_text
    if _wv_from_text is None:
        start_time = time.time()
        print('-*-*-*-*-*-*Loading Word2Vec model*-*-*-*-*-*-')
        print('estimated time: {}'.format(13.6 / 1000000 * _MAX_WORD_COUNT))
        _wv_from_text = KeyedVectors.load_word2vec_format(
            _tencent_file, binary=True)
        _wv_from_text.init_sims(replace=True)
        print(
            '-*-*-*-*-*-*Finished, use {}*-*-*-*-*-*-'.format(time.time() - start_time))
    noword = set()

    def convert_word2vec(words: list):
        cnt = 0.0
        res = np.zeros(200)
        for word in words:
            try:
                res += _wv_from_text.get_vector(word)
                cnt += 1.0
            except Exception:
                noword.add(word)
        if cnt > 0:
            res = res / cnt
        return res

    data_X = list()
    for comment in comments:
        data_X.append(convert_word2vec(
            _filter_stop_words(jieba_cut_comment(comment))))
    print('cannot find {} words, {}'.format(len(noword), list(noword)))
    data_X = pd.DataFrame(data_X)
    print(data_X.head())
    return data_X


_model: MLPClassifier = None
_model_path = './static/MLP120_120.pkl'


def _mlp_pred(x_test):
    global _model
    if _model is None:
        with open(_model_path, 'rb') as f:
            _model = pickle.load(f)
    return _model.predict(x_test)


def _result2list(comments: pd.Series, y_pred: np.ndarray) -> Dict:
    aspect_list = ['功能', '性能', '安全', '可靠', '易用']
    res = dict()
    for aspect in aspect_list:
        res.setdefault(aspect, dict())
    label2aspect_index = [1, 3, 0, 3, 0, 0, 0, 3, 3, 2, 2, 1, 1, 1, 3, 4]
    for i in range(len(label2aspect_index)):
        label = label_list[i]
        aspect = aspect_list[label2aspect_index[i]]
        res[aspect].setdefault(label, [])
    rows, cols = y_pred.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            if y_pred[i, j] == 1:
                label = label_list[j]
                aspect = aspect_list[label2aspect_index[j]]
                comment = comments[i]
                res[aspect][label].append(comment)
    return res


def classify_comments(file):
    df = pd.read_csv(file, encoding='utf-8')
    if 'class' in df.columns:
        df = df[lambda x: x['class'] != 'best'].reset_index(drop=True)
    # print(df.shape)
    # print(df.head())

    x_test = _tencent_embedding(df['comments'])
    y_pred = _mlp_pred(x_test)
    return _result2list(df['comments'], y_pred)

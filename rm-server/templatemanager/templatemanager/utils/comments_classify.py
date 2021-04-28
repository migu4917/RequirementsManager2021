import pickle
import numpy as np
import pandas as pd
from gensim.models import KeyedVectors
import time
from sklearn.neural_network import MLPClassifier
from typing import List

_tencent_file = '../tecent_ailab_word2vec/Tencent_AILab_ChineseEmbedding_2M.twv'
_wv_from_text = None
_MAX_WORD_COUNT = 2000000


def tencent_embedding(comments: pd.Series) -> pd.DataFrame:
    global _wv_from_text
    if _wv_from_text == None:
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
            filter_stop_words(jieba_cut_commment(comment))))
    print('cannot find {} words, {}'.format(len(noword), list(noword)))
    data_X = pd.DataFrame(data_X)
    print(data_X.head())
    return data_X


_model = None
_model_path = './MLP120_120.pkl'


def mlp_pred(x_test):
    global _model
    if _model == None:
        with open(_model_path, 'rb') as f:
            _model = pickle.load(f)
    return _model.predict(x_test)


def result2list(df: pd.DataFrame) -> List:
    pass


def comments_classsify(file):
    df = pd.DataFrame(file)
    return df

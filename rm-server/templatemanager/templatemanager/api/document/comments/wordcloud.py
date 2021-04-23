import os

from flask import request
from templatemanager.app import app

import jieba
import wordcloud

META_SUCCESS = {'status': 200, 'msg': '创建成功！'}
META_ERROR_BAD_FILE = {'status': 404, 'msg': '生成失败，评论集不存在！'}


@app.route('/document/comments/wordcloud', methods=[''])
def comments_wordcloud():
    # todo
    return {'meta': META_SUCCESS}

import os

from flask import request
from templatemanager.app import app
from templatemanager.dao.document import (
    Document, DocumentMongoDBDao
)
from templatemanager.mongodb import document_collection
from templatemanager.config import UPLOAD_FILE_DIRNAME
from templatemanager.utils.handle_api import handle_response
from templatemanager.utils.comments_wordcloud import generateWordCloudBase64
import jieba
import wordcloud

META_SUCCESS = {'status': 200, 'msg': '创建成功！'}
META_ERROR_BAD_FILE = {'status': 404, 'msg': '生成失败，评论集不存在！'}


@app.route('/document/comments/wordcloud', methods=['GET'])
@handle_response
def comments_wordcloud():
    # todo
    return {'meta': META_SUCCESS}

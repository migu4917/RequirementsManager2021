import os

from flask import request
from templatemanager.app import app

from templatemanager.dao.document import (
    Document, DocumentMongoDBDao
)
from templatemanager.mongodb import document_collection
from templatemanager.config import UPLOAD_FILE_DIRNAME
from templatemanager.utils.handle_api import handle_response
from templatemanager.utils.comments_classify import comments_classsify

META_SUCCESS = {'status': 200, 'msg': '分析成功！'}
META_WRONG_FORMAT = {'status': 400, 'msg': '数据格式错误！'}
META_ERROR = {'status': 404, 'msg': '评论数据不存在！'}


@app.route('/document/comments/classsify', methods=['POST'])
@handle_response
def comments_classsify():
    body = request.json

    comments_file_name = body['comments_file_name']

    return {'meta': META_SUCCESS}

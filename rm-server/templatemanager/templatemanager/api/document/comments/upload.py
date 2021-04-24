import os

from flask import request
from templatemanager.app import app

from templatemanager.dao.document import (
    Document, DocumentMongoDBDao
)

from templatemanager.utils.handle_api import handle_response

META_SUCCESS = {'status': 200, 'msg': '创建成功！'}
META_ERROR_BAD_FILE = {'status': 400, 'msg': '上传失败，文件格式错误！'}


@app.route('/document/comments/upload', methods=['PUT'])
@handle_response
def comments_upload():
    # body = request.json

    upload_file = request.files['file']
    if not upload_file.filename.endswith('.csv'):
        return {'meta': META_ERROR_BAD_FILE}

    filename = os.path.splitext(upload_file.filename)[0]
    # TODO

    return {
        'meta': META_SUCCESS,
        'data': {
            
        }
    }

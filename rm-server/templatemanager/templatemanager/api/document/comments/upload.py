import os

from flask import request
from templatemanager.app import app

from templatemanager.utils.handle_api import handle_response

META_SUCCESS = {'status': 200, 'msg': '创建成功！'}


@app.route('document/comments/upload', methods=['PUT'])
@handle_response
def comments_upload():
    body = request.json
    return META_SUCCESS

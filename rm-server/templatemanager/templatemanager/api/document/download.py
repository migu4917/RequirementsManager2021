import os

from flask import request
from templatemanager.app import app
from templatemanager.dao.document import (
    Document, DocumentMongoDBDao
)
from templatemanager.mongodb import document_collection
from templatemanager.utils.handle_api import handle_response
from templatemanager.utils.uuid import generate_uuid

META_SUCCESS = {'status': 200, 'msg': '下载成功！'}
META_ERROR_ALREADY_EXIST = {'status': 400, 'msg': '创建失败，该模板已存在！'}
META_ERROR_NO_FILE = {'status': 404, 'msg': '创建失败，文件不存在！'}


@app.route('document/download', methods=['GET'])
@handle_response
def document_download():
    body = request.json
    return META_SUCCESS

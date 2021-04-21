import os

from flask import request
from templatemanager.app import app
from templatemanager.dao.document import (
    Document, DocumentMongoDBDao
)
from templatemanager.mongodb import document_collection
from templatemanager.utils.handle_api import handle_response
from templatemanager.utils.uuid import generate_uuid

META_SUCCESS = {'status': 200, 'msg': '获取成功！'}
META_ERROR_NO_DOCUMENT = {'status': 404, 'msg': '获取失败，文档不存在！'}


@app.route('document/list', methods=['GET'])
@handle_response
def document_list():
    body = request.json
    return {'meta': META_SUCCESS}

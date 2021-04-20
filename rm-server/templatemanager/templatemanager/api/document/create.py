import os

from flask import request
from templatemanager.app import app
from templatemanager.dao.document import (
    Document, DocumentMongoDBDao
)
from templatemanager.mongodb import document_collection
from templatemanager.utils.handle_api import handle_response
from templatemanager.utils.uuid import generate_uuid

from time import asctime, localtime

META_SUCCESS = {'status': 200, 'msg': '创建成功！'}
META_ERROR_ALREADY_EXIST = {'status': 400, 'msg': '创建失败，该模板已存在！'}
META_ERROR_NO_FILE = {'status': 404, 'msg': '创建失败，文件不存在！'}


@app.route('document/create', methods=['POST'])
@handle_response
def document_create():
    body = request.json
    return META_SUCCESS

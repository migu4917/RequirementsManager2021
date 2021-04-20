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
META_ERROR_NO_FILE = {'status': 404, 'msg': '下载失败，文档不存在！'}


@app.route('document/download', methods=['GET'])
@handle_response
def document_download():
    body = request.json

    document_id = body['document_id']

    document_mongodb_dao = DocumentMongoDBDao(document_collection)

    document = document_mongodb_dao.get_document(document_id)

    if not document:
        return {'meta': META_ERROR_NO_FILE}

    # TODO

    return {'meta': META_SUCCESS}

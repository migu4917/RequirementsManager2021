import os

from flask import request
from templatemanager.app import app

from templatemanager.dao.document import (
    Document, DocumentMongoDBDao
)
from templatemanager.mongodb import document_collection
from templatemanager.utils.handle_api import handle_response


@app.route('/document/comments/similarity', methods=['POST'])
@handle_response
def comments_similarity():
    body = request.json
    pass

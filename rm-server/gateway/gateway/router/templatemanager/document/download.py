from flask import request

from gateway.app import app
from gateway.utils.handle_api import (
    get_client_username, handle_request_response, handle_download
)
from gateway.http_client import templatemanager_http_client


@app.route('/document/download', methods=['GET'])
@handle_download
@get_client_username
def document_download(client_username: str):
    body = request.json
    return templatemanager_http_client.get(
        'document/download', client_username, json=body
    )

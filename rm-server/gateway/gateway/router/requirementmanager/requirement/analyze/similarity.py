from flask import request

from gateway.app import app
from gateway.http_client import requirementmanager_http_client
from gateway.utils.handle_api import (
    get_client_username, handle_request_response
)


@app.route('/requirement/analyze/similarity', methods=['POST'])
@handle_request_response
@get_client_username
def requirement_analyze_similarity(client_username: str):
    body = request.json
    status_code, resp_body = requirementmanager_http_client.post(
        'requirement/analyze/similarity', client_username, json=body
    )
    return status_code, resp_body

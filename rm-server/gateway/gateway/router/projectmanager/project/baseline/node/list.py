from flask import request

from gateway.app import app
from gateway.http_client import projectmanager_http_client
from gateway.utils.handle_api import (
    get_client_username, handle_request_response
)


@app.route('/project/baseline/node/list', methods=['GET'])
@handle_request_response
@get_client_username
def project_baseline_node_list(client_username: str):
    args = request.args.to_dict()
    status_code, resp_body = projectmanager_http_client.get(
        'project/baseline/node/list', client_username, params=args
    )
    return status_code, resp_body

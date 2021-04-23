from flask import request

from gateway.app import app
from gateway.utils.handle_api import (
    get_client_username, handle_request_response
)
from gateway.http_client import templatemanager_http_client

# todo
@app.route('/document/comments/classify', methods=[''])
@handle_request_response
@get_client_username
def comments_wordcloud(client_username: str):
    pass
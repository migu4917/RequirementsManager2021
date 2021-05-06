import json
from typing import Callable
from functools import wraps
import traceback
from flask import request, Response

from gateway.authtoken import token_storage


def handle_request_response(func: Callable):

    @wraps(func)
    def _func(*args, **kwargs):
        print("request.headers: \n" + str(request.headers))
        print("request.data: \n" + str(request.data))
        status_code = None
        try:
            status_code, resp_body = func(*args, **kwargs)
        except Exception as e:
            print("Error During Function Excution!!!!")
            print('Exception is ---')
            print(e)
            print(traceback.print_exc())
            resp_body = {'meta': {'status': 500, 'msg': 'Internal Server Error'}}

        if status_code and status_code != 200:
            print("Error status_code {}".format(status_code))
            resp_body = {'meta': {'status': 500, 'msg': 'Internal Server Error'}}
        print(resp_body)
        return Response(json.dumps(resp_body), mimetype='application/json')

    return _func


# def handle_download(func: Callable):
#     @wraps(func)
#     def _func(*args, **kwargs):
#         print(request.headers)
#         print(request.data)

#         return Response(func(*args, **kwargs), mimetype='application/msword')
    
#     return _func


def get_client_username(func: Callable):

    @wraps(func)
    def _func(*args, **kwargs):
        token_value = request.headers.get('Authorization', None)
        if not token_value:
            return 200, {'meta': {'status': 401, 'msg': '身份认证失败！'}}
        client_username = token_storage.get_username(token_value)
        if not client_username:
            return 200, {'meta': {'status': 401, 'msg': '身份认证失败！'}}
        return func(*args, client_username=client_username, **kwargs) 

    return _func

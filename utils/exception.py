# coding: utf8
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler


def api_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        status_code = getattr(type(exc), 'status_code', 404)
        code = getattr(type(exc), 'code', status_code)

        data = {}
        if status_code == status.HTTP_401_UNAUTHORIZED:
            request = context.get("request")
            data['sso-server'] = '{}://{}{}'.format(request.scheme, request.get_host(), "/api/v1/sso/login")

        msg = response.data.get('detail', response.data)

        # 处理序列化返回信息
        if isinstance(msg, dict):
            msg = list(msg.values())[0][0]
        res = {
            "code": code,
            "msg": msg,
            "data": data,
        }

        response.data = res
        response.status_code = 200

    return response


class ParamError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "bad request"


class Unauthorized(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "unauthorized, user not login or token was expired"


class Forbidden(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "permission denied"


class NotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "not found"

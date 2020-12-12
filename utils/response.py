# coding: utf8
import json

from django.http import HttpResponse
from rest_framework import status


class ApiResponse(HttpResponse):
    status_code = 200
    msg = "成功！"
    data = {}
    content_type = "application/json"
    charset = 'utf8'
    code = 0

    def __init__(self, msg=None, code=None, data=None):
        if code:
            self.code = code
        if msg is not None:
            self.msg = msg
        if data is not None:
            self.data = data
        res = {"code": self.code, "msg": self.msg, 'data': self.data}
        res = json.dumps(res, ensure_ascii=False, allow_nan=False, separators=(',', ':'))
        res = res.replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
        super().__init__(content=res.encode(), content_type=self.content_type, charset=self.charset)


class BadRequestResponse(ApiResponse):
    code = status.HTTP_400_BAD_REQUEST
    message = "bad request"


class UnauthorizedResponse(ApiResponse):
    code = status.HTTP_401_UNAUTHORIZED
    message = "unauthorized, user not login or token was expired"


class ForbiddenResponse(ApiResponse):
    code = status.HTTP_403_FORBIDDEN
    message = "permission denied"


class PageNotFoundResponse(ApiResponse):
    code = status.HTTP_404_NOT_FOUND
    message = "page not found"


class ServerErrorResponse(ApiResponse):
    code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "internal server error"

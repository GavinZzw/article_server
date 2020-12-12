# coding: utf8
import re
from _sha1 import sha1

from django.utils.deconstruct import deconstructible
from rest_framework.exceptions import ValidationError


class RegexValidator:
    regex = ''
    message = ''

    def __call__(self, value):
        regex_matches = re.match(self.regex, str(value))
        if regex_matches is None:
            raise ValidationError(self.message, )


@deconstructible
class UsernameValidator(RegexValidator):
    regex = r'^[a-zA-Z0-9][\w@.-]+$'
    message = 'Illegal username. It must start with [a-z0-9], and contain only letters, numbers, and @/./-/_ '


@deconstructible
class NameValidator(RegexValidator):
    regex = r'^\w+$'
    message = 'This value may contain only letters, numbers, and _'


@deconstructible
class NoneSpecialValidator(RegexValidator):
    regex = r'^[\w.@+-]+$'
    message = 'This value may contain only letters, numbers, and _/./@/+/-'


@deconstructible
class NonSpaceValidator(RegexValidator):
    regex = r'^\S+$'
    message = "This value may contain only non-space."


@deconstructible
class ServerPortValidator(RegexValidator):
    regex = r'^[1-9]\d{0,4}$'
    message = "Port must be number and between 1 - 65535"

    def __call__(self, value):
        regex_matches = re.match(self.regex, str(value))
        if (regex_matches is None) or (int(value) > 65535):
            raise ValidationError(self.message, )


def encrypt_password(pwd):
    s1 = sha1()
    s1.update(pwd.encode('utf-8'))
    hpwd = s1.hexdigest()
    return hpwd

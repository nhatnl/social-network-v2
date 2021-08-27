import re

from rest_framework import serializers
from django.utils.translation import gettext as _

class PasswordValidation:
    """
        Validation For password has as least 8 char mus has number and character
    """
    message = _('password must has 8 char length and has number and alphabe char')

    def __init__(self, password_field = 'password', message=None) -> None:
        self.password_field = password_field
        self.message = message or self.message

    def __call__(self, attrs):
        if re.fullmatch('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', attrs[self.password_field]) is None:
            message = self.message
            raise serializers.ValidationError(message, code='password_invalid')

    def validate(self, password, user=None):
        if re.fullmatch('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password) is None:
            message = self.message
            raise serializers.ValidationError(message, code='password_invalid')
            
    def get_help_text(self):
        return _('Your Password must have number, alpha ...')
import uuid

import timeflake
from django import forms
from django.core import exceptions
from django.db import models


def _parse(value) -> timeflake.Timeflake:
    pass


class TimeflakeBinary(models.Field):
    description = "Timeflake UUID (128-bit)"

    def __init__(self, *args, **kwargs):
        pass

    def deconstruct(self):
        pass

    def db_type(self, connection):
        pass

    def rel_db_type(self, connection):
        pass

    def from_db_value(self, value, expression, connection):
        pass

    def to_python(self, value):
        pass

    def get_db_prep_value(self, value, connection, prepared=False):
        pass

    def formfield(self, **kwargs):
        pass


class TimeflakePrimaryKeyBinary(TimeflakeBinary):
    def __init__(self, *args, **kwargs):
        pass

    def deconstruct(self):
        pass

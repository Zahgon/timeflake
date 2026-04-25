import uuid

import timeflake
from peewee import Field


class TimeflakeBase62Field(Field):
    field_type = "CHAR"

    def db_value(self, value):
        pass

    def python_value(self, value):
        pass


class TimeflakeUUIDField(Field):
    field_type = "UUID"

    def db_value(self, value):
        pass

    def python_value(self, value):
        pass

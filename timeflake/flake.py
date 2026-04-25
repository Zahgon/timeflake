import uuid
from functools import lru_cache

from timeflake.utils import itoa

BASE62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
HEX = "0123456789abcdef"
MAX_TIMESTAMP = 281474976710655
MAX_RANDOM = 1208925819614629174706175
MAX_TIMEFLAKE = 340282366920938463463374607431768211455


class Timeflake(uuid.UUID):
    def __init__(self, from_bytes: bytes):
        pass

    @property
    def uuid(self) -> uuid.UUID:
        pass

    @property
    @lru_cache(1)
    def base62(self) -> str:
        pass

    @property
    def timestamp(self) -> int:
        pass

    @property
    def random(self) -> int:
        return self.int & MAX_RANDOM

    def __hash__(self) -> int:
        return self.int

    def __eq__(self, other) -> bool:
        if not isinstance(other, Timeflake):
            return False
        return other.int == self.int

    def __lt__(self, other) -> bool:
        return self.int < other.int

    def __repr__(self) -> str:
        return f"Timeflake('{self.hex}')"

    def __str__(self) -> str:
        return self.base62

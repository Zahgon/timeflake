__version__ = "0.4.3"
__all__ = ["Timeflake", "random", "from_values"]

import os
import time
from typing import Optional

from timeflake.flake import BASE62, HEX, Timeflake
from timeflake.utils import atoi


def parse(
    from_bytes: bytes = None, from_int=None, from_hex=None, from_base62=None
) -> Timeflake:
    pass


def random() -> Timeflake:
    timestamp = int(time.time() * 1000)
    rand = int.from_bytes(os.urandom(10), "big", signed=False)
    value = ((timestamp << 80) | rand).to_bytes(16, "big")
    return Timeflake(from_bytes=value)


def from_values(timestamp: int, random: Optional[int] = None) -> Timeflake:
    pass

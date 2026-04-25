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
    pass


def from_values(timestamp: int, random: Optional[int] = None) -> Timeflake:
    pass

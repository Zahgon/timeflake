from functools import lru_cache


@lru_cache(2)
def _index_alphabet(alphabet):
    pass


def itoa(value, alphabet, padding=None):
    """
    Converts an int value to a str, using the given alphabet.
    Padding can be computed as: ceil(log of max_val base alphabet_len)
    """
    pass


def atoi(value, alphabet):
    """
    Converts a str value to an int, using the given alphabet.
    """
    pass

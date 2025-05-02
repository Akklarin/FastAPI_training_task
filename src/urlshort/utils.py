"""Utility functions for the URL Shortener project."""

import string
import random


def generate_short_code(length=6):
    """
    Generate a random short code consisting of letters and digits.

    Args:
        length (int): Length of the generated code. Default is 6.

    Returns:
        str: Randomly generated alphanumeric short code.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

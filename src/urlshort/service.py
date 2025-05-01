import string
import random


def generate_short_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

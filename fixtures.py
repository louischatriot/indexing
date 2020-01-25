import uuid
import random

def encode_to_word(i):
    return encode_with_alphabet(i, "abcdefghijklmnopqrstuvwxyz")


def encode_with_alphabet(i, alphabet):
    b = len(alphabet)
    result = ""

    while i != 0:
        r = i % b
        result = alphabet[r] + result
        i = int((i - r) / b)

    return result


def generate_word():
    s = ""
    while len(s) < 10:
        s += encode_to_word(uuid.uuid4().int)

    s = s[0:10]
    return s


def generate_number(s=0, e=1000):
    return random.randrange(s, e)


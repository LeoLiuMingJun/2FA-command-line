import base64
import hashlib
import hmac
import struct
import time
import os
import pyperclip


def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = h[19] & 15
    h = (struct.unpack(">I", h[o:o + 4])[0] & 0x7fffffff) % 1000000
    return '{0:06d}'.format(h)


def get_totp_token(secret):
    return get_hotp_token(secret, intervals_no=int(time.time()) // 30)

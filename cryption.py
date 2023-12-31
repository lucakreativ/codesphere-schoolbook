from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from datetime import datetime
import base64
from binascii import unhexlify, b2a_base64
from read_config import read_aes_config
import hashlib

import string
import random

KEYSIZE = 16
BLOCKSIZE = 16


def totp():
    config=read_aes_config()

    key=config["password"]
    iv=config["iv"]
    day=int(config["day"])
    month=int(config["month"])
    year=int(config["year"])

    dt1=datetime(day=day, month=month, year=year)
    now=datetime.now()
    timedelta=now-dt1
    days=timedelta.days

    hash_res=hashlib.sha512((str(key)+str(days)).encode("utf-8")).hexdigest()
    
    key=hash_res[0:16]

    return key, iv


def encrypt(plaintext):
    key, iv=totp()
    
    key=key.encode("ascii")
    iv=iv.encode("ascii")

    cipher1 = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher1.encrypt(pad(plaintext.encode(), BLOCKSIZE))

    ciphertext=(base64.urlsafe_b64encode(ciphertext)).decode("ascii")
    return ciphertext

def decrypt(ciphertext):
    key, iv=totp()

    key=key.encode("ascii")
    iv=iv.encode("ascii")

    ciphertext=ciphertext.encode("ascii")
    ciphertext=base64.urlsafe_b64decode(ciphertext)

    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    plaintext2 = unpad(cipher2.decrypt(ciphertext), BLOCKSIZE)


    return plaintext2.decode()


def generate_password(length):
    number=random.choice(list(string.digits))
    low_char=random.choice(list(string.ascii_lowercase))
    up_char=random.choice(list(string.ascii_uppercase))
    password=[number, low_char, up_char]
    characters=list(string.ascii_letters + string.digits)
    password+=random.choices(characters, k=length-3)
    random.shuffle(password)

    password_string="".join(password)

    return password_string
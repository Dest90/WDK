#!/usr/bin/env python
#-*-coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto import Random
from binascii import unhexlify
from Crypto.Util import Counter
import os

plik = open('ctr.txt', 'r')
czytany = plik.read().splitlines()
key = unhexlify(czytany[0])
iv = unhexlify(czytany[1])
ctr = Counter.new(128)
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
msg = iv + cipher.decrypt(unhexlify(czytany[2]))
print cipher.decrypt(msg).decode('latin-1')

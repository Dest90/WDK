#!/usr/bin/env python
#-*-coding: utf-8 -*-
import hashlib

plik= open('plik.pdf','rb')
try:
    czytany = plik.read();
finally:
    plik.close()
sh=hashlib.sha256(czytany).hexdigest()
print "SHA 256: %s"%sh
md=hashlib.md5(czytany).hexdigest()
print "MD 5: %s"%md

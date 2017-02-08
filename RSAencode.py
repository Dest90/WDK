#!/usr/bin/python

from Crypto.PublicKey import RSA
from Crypto import Random

def main():
    with open('publicKeyFile.pem', 'r') as klucz_publiczny:
        plik = raw_input("Podaj nazwe pliku do zaszyfrowania: ")
        plik_szyfrowany = open(plik, 'r')
        plik_zaszyfrowany = open('zaszyfrowany.txt', 'w')
        klucz_pub = RSA.importKey(klucz_publiczny.read())
        wiadomosc = plik_szyfrowany.read()
        szyfr = klucz_pub.encrypt(wiadomosc, 32)
        plik_zaszyfrowany.write(szyfr[0].encode('hex'))

        plik_szyfrowany.close()
        plik_zaszyfrowany.close()

if __name__ == "__main__":
    main()

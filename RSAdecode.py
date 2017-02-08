#!/usr/bin/python

from Crypto.PublicKey import RSA
from Crypto import Random

def main():
    with open('privateKeyFile.pem', 'r') as klucz_prywatny:
        plik = raw_input("Podaj nazwe pliku do zdekodowania: ")
        plik_szyfrowany = open(plik, 'r')
        plik_odszyfrowany = open('odszyfrowany.txt', 'w')
        klucz_pryw = RSA.importKey(klucz_prywatny.read())
        szyfr = (plik_szyfrowany.read()).decode('hex')
        wiadomosc = klucz_pryw.decrypt(szyfr)
        plik_odszyfrowany.write(wiadomosc)

        plik_szyfrowany.close()
        plik_odszyfrowany.close()

if __name__ == "__main__":
    main()

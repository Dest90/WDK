#!/usr/bin/python

from Crypto.PublicKey import RSA
from Crypto import Random

def main():

    liczba = Random.new().read
    klucz = RSA.generate(4096, liczba)
    klucz_prywatny = open("privateKeyFile.pem", 'w')
    klucz_prywatny.write(klucz.exportKey(format='PEM'))
    klucz_publiczny = open("publicKeyFile.pem", 'w')
    klucz_publiczny.write(klucz.publickey().exportKey(format='PEM'))
    klucz_publiczny.close()
    klucz_prywatny.close()

if __name__ == "__main__":
    main()

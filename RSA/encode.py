import rsa
with open('pubkey.pem') as publiczny:
	keydata = publiczny.read()
	pubkey =  rsa.PublicKey.load_pkcs1(keydata)
from rsa.bigfile import *
with open('plik.pdf', 'rb') as infile, open('encode.txt', 'wb') as wynik:
	encrypt_bigfile(infile, wynik, pubkey)
plik= open("encode.txt","r")

czytany= plik.read()
plik.close()
zapis= open("encode.txt","w")
zapis.write(czytany.encode("hex"))
zapis.close()

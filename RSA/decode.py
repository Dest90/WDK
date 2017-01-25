import rsa
plik= open("encode.txt","r")
czytany= plik.read()
plik.close()
zapis= open("encode.txt","w")
zapis.write(czytany.decode("hex"))
zapis.close()
with open('privkey.pem') as prywatny:
	keydata = prywatny.read()
	privkey =  rsa.PrivateKey.load_pkcs1(keydata)
from rsa.bigfile import *
with open('encode.txt', 'rb') as infile, open('decode.pdf', 'wb') as wynik:
	decrypt_bigfile(infile, wynik, privkey)

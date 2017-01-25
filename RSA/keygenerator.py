import rsa
(klucz_publiczny, klucz_prywatny) = rsa.newkeys(256, poolsize=2)
print(klucz_publiczny)
print(klucz_prywatny)
publiczny=klucz_publiczny.save_pkcs1('PEM')
plik= open('pubkey.pem','w')
plik.write(publiczny)

prywatny=klucz_prywatny.save_pkcs1('PEM')
plik= open('privkey.pem','w')
plik.write(prywatny)

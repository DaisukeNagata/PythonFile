from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA512
import binascii

def start_Key():

    rsa_key = RSA.generate(bits=2048)
    key = RSA.construct(map(int, (rsa_key.n,rsa_key.e,rsa_key.d)))

    private = key.exportKey()
    public = key.publickey().exportKey()

    print(private)

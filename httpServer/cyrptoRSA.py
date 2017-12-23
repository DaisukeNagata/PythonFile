from Crypto.PublicKey import RSA

def start_Key():

    rsa_key = RSA.generate(bits=2048)
    key = RSA.construct(map(int, (rsa_key.n,rsa_key.e,rsa_key.d)))

    private = key.exportKey()
    public = key.publickey().exportKey()
    print(public)
    return public


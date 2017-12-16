from Crypto.PublicKey import RSA
import Crypto.PublicKey.RSA as RSA

def main():
    rsa_fact = RSA.RSAImplementation()
    rsa_key = rsa_fact.generate(bits=2048)
    
    key = RSA.construct(map(int, (rsa_key.n,rsa_key.e,rsa_key.d)))

    private = key.exportKey()
    public = key.publickey().exportKey()

    f = open('private-key.pem', 'wb')
    f.write(private)
    f.close()

    f = open('public-key.pem', 'wb')
    f.write(public)
    f.close()

if __name__=='__main__':
    main()


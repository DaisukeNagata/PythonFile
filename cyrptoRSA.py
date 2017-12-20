from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA512
import binascii

def main():

    rsa_key = RSA.generate(bits=2048)
    
    key = RSA.construct(map(int, (rsa_key.n,rsa_key.e,rsa_key.d)))

    private = key.exportKey()
    public = key.publickey().exportKey()

    f = open('private-key.pem', 'wb')
    f.write(private)
    f.close()

    print(private)
    f = open('public-key.pem', 'wb')
    f.write(public)
    f.close()

    print(public)
    message = u'暗号化'.encode('utf-8')
    P = binascii.b2a_hex(message)
    key = rsa_key
    cipher = PKCS1_OAEP.new(key, hashAlgo=SHA512)
    ciphertext = cipher.encrypt(P)
    
    f = open('msg.bin', 'w')
    f.write('文字列の代入')
    f.close()
    
    'ターミナルコマンド->openssl rsautl -encrypt -pubin -inkey 出力.pem -in msg.bin -out 作成binファイル'
    
    
    print(ciphertext)
    M = cipher.decrypt(ciphertext)
    message = binascii.a2b_hex(M).decode('utf-8')
    print(message)
    
if __name__=='__main__':
    main()


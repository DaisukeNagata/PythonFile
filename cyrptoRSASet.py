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
    
    private_cipher = PKCS1_OAEP.new(key, hashAlgo=SHA512)
    message2 = private_cipher.decrypt(ciphertext).decode('utf-8')

    print('暗号化')
    print(ciphertext)
    
    print('複合化')
    print(message2)
    
    # https://qiita.com/kunichiko/items/12cbccaadcbf41c72735
    # openssl rsa -in private-key.pem -text -noout 秘密鍵の中身を見る方法
    # openssl rsa -pubin -in public-key.pem -text -noout 公開鍵の中身を見る方法
    # openssl x509 -in public-key.der.crt -inform der -out public-key.crt 証明書(署名付きの公開鍵)を作成する
    # openssl req -in my-request.csr -text -noout CSRの中身を表示する
    # openssl x509 -req -in my-request.csr -CA ca-crt.pem -CAkey ca-private-key.pem -CAcreateserial -days 3650 -out public-key.crt CSRから証明書を発行する
    # ca-crt.pemをCAに依頼
    # openssl x509 -req -in my-request.csr -signkey private-key.pem -out public-key.crt -days 3650
    # openssl x509 -req -in my-request.csr -signkey private-key.pem -out public-key.crt -days 3650 自己署名証明書を発行する場合
if __name__=='__main__':
    main()


from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

def exportPK():
    with open("private_key.pem", "r") as src:
        private_key = RSA.importKey(src.read())

    public_key = private_key.publickey()

    with open('public_key.txt', 'w') as out:
        out.write(public_key.exportKey().decode('utf-8'))
    return public_key,private_key
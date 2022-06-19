import sys

from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA



def verify(message, sig):


    digest = SHA256.new()
    digest.update(message.encode('utf-8'))


    sig = bytes.fromhex(sig)  # convert string to bytes object

    # Load public key and verify signature
    public_key = RSA.importKey(open("public_key.txt").read())
    verifier = PKCS1_v1_5.new(public_key)
    verified = verifier.verify(digest, sig)

    if verified:
        print('Successfully verified message')
    else:
        print('FAILED')
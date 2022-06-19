from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA


def sign(msg, private_key):
    # message = "I want this stream signed"
    digest = SHA256.new()
    digest.update(msg.encode('utf-8'))

    # Sign the message
    signer = PKCS1_v1_5.new(private_key)
    sig = signer.sign(digest)

    print("Signature:")
    return sig.hex()


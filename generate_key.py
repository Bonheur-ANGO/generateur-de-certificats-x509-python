
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, ec, dsa, ed448, ed25519
import json


with open("certification_autorithy.json", "r") as certification:
    CA = json.load(certification)

#génération de la clé privée avec l'algorithme de signature
def generate_key(signature):
    key = None
    if key is None:
        if signature == "RSA":
            key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )
        if signature == "DSA":
            key = dsa.generate_private_key(
                key_size=2048,
                backend=default_backend()
            )
        if signature == "EC":
            key = ec.generate_private_key(
                ec.SECP384R1()
            )
        if signature == "ED448":
            key = ed448.Ed448PrivateKey.generate()
        if signature == "ED25519":
            key = ed25519.Ed25519PrivateKey.generate()
        return key


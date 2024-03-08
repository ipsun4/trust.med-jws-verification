import base64
import json
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization
import jwt


def generate_jwt():

    keys = json.load(open("keys.json"))
    pem_formatted_private_key = (Ed25519PrivateKey.from_private_bytes(base64.b64decode(keys["private_key"]))
                                 .private_bytes(
        encoding=serialization.Encoding.PEM,
        encryption_algorithm=serialization.NoEncryption(),
        format=serialization.PrivateFormat.PKCS8
        ))

    token = jwt.encode({"payload": "lorem ipsum"}, pem_formatted_private_key, algorithm="EdDSA")

    with open("jwt.txt", "w") as token_file:
        token_file.write(token)


if __name__ == '__main__':
    generate_jwt()
